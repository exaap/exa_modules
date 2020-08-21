# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_round


class StockQuant(models.Model):
    _inherit = "stock.quant"

    @api.multi
    def _quant_update_from_move_recalculation(self, move, location_dest_id,
                                              dest_package_id, lot_id=False,
                                              entire_pack=False):
        vals = {
            'location_id': location_dest_id.id,
            'history_ids': [(4, move.id)],
            'reservation_id': False}

        if lot_id and any(quant for quant in self if not quant.lot_id.id):
            vals['lot_id'] = lot_id

        if not entire_pack:
            vals.update({'package_id': dest_package_id})

        self.write(vals)

    @api.model
    def _quant_create_from_move_recalculation(self, qty, move, lot_id=False,
                                              owner_id=False, src_package_id=False,
                                              dest_package_id=False,
                                              force_location_from=False,
                                              force_location_to=False):
        '''Create a quant in the destination location and create a negative
        quant in the source location if it's an internal location. '''
        price_unit = move.get_price_unit()
        location = force_location_to or move.location_dest_id
        rounding = move.product_id.uom_id.rounding
        vals = {
            'product_id': move.product_id.id,
            'location_id': location.id,
            'qty': float_round(qty, precision_rounding=rounding),
            'cost': price_unit,
            'history_ids': [(4, move.id)],
            'in_date': move.date,
            'company_id': move.company_id.id,
            'lot_id': lot_id,
            'owner_id': owner_id,
            'package_id': dest_package_id}

        if move.location_id.usage == 'internal':
            # if we were trying to move something from an internal location
            # and reach here (quant creation), it means that a negative quant
            # has to be created as well.
            location_id = (
                force_location_from.id if force_location_from else move.location_id.id)
            negative_vals = vals.copy()
            negative_vals['location_id'] = location_id
            negative_vals['qty'] = float_round(-qty, precision_rounding=rounding)
            negative_vals['cost'] = price_unit
            negative_vals['negative_move_id'] = move.id
            negative_vals['package_id'] = src_package_id
            negative_quant_id = self.sudo().create(negative_vals)
            vals.update({'propagated_from_id': negative_quant_id.id})

        picking_type = move.picking_id.picking_type_id if move.picking_id else False

        if (lot_id and move.product_id.tracking == 'serial'
                and ((picking_type.use_create_lots or picking_type.use_existing_lots)
                     or not picking_type)):
            if qty != 1.0:
                raise UserError(
                    _('You should only receive by the piece with the same serial number'))

        # create the quant as superuser, because we want to restrict the creation of
        # quant manually: we should always use this method to create quants
        return self.sudo().create(vals)

    @api.model
    def quants_move_recalculation(self, quants, move, location_to, location_from=False,
                                  lot_id=False, owner_id=False, src_package_id=False,
                                  dest_package_id=False, entire_pack=False):
        """Moves all given stock.quant in the given destination location.
            Unreserve from current move.
        :param quants: list of tuple(browse record(stock.quant) or None, quantity to move)
        :param move: browse record (stock.move)
        :param location_to: browse record (stock.location) depicting where the quants
            have to be moved
        :param location_from: optional browse record (stock.location) explaining
            where the quant has to be taken (may differ from the move source location
            in case a removal strategy applied). This parameter is only used to pass
            to _quant_create_from_move_racalculation if a negative quant must be created
        :param lot_id: ID of the lot that must be set on the quants to move
        :param owner_id: ID of the partner that must own the quants to move
        :param src_package_id: ID of the package that contains the quants to move
        :param dest_package_id: ID of the package that must be set on the moved quant
        """
        # TDE CLEANME: use ids + quantities dict
        if location_to.usage == 'view':
            raise UserError(
                _('You cannot move to a location of type view %s.')
                % (location_to.name))

        quants_reconcile_sudo = self.env['stock.quant'].sudo()
        quants_move_sudo = self.env['stock.quant'].sudo()
        check_lot = False

        for quant, qty in quants:
            if not quant:
                # If quant is None, we will create a quant to move
                # (and potentially a negative counterpart too)
                quant = self._quant_create_from_move_recalculation(
                    qty,
                    move,
                    lot_id=lot_id,
                    owner_id=owner_id,
                    src_package_id=src_package_id,
                    dest_package_id=dest_package_id,
                    force_location_from=location_from,
                    force_location_to=location_to)
                check_lot = True
            else:
                quant._quant_split(qty)
                quants_move_sudo |= quant
            quants_reconcile_sudo |= quant

        if quants_move_sudo:
            # moves_recompute = quants_move_sudo.\
            #    filtered(lambda self: self.reservation_id != move).\
            #        mapped('reservation_id')

            quants_move_sudo._quant_update_from_move_recalculation(
                move,
                location_to,
                dest_package_id,
                lot_id=lot_id,
                entire_pack=entire_pack)

            # moves_recompute.recalculate_move_state()

        if location_to.usage == 'internal':
            # Do manual search for quant to avoid full table scan (order by id)
            self._cr.execute("""
                SELECT 0
                FROM stock_quant, stock_location
                WHERE product_id = %s
                AND stock_location.id = stock_quant.location_id
                AND ((stock_location.parent_left >= %s
                AND stock_location.parent_left < %s) OR stock_location.id = %s)
                AND qty < 0.0 LIMIT 1""", (
                    move.product_id.id,
                    location_to.parent_left,
                    location_to.parent_right,
                    location_to.id))

            if self._cr.fetchone():
                quants_reconcile_sudo._quant_reconcile_negative(move)

        # In case of serial tracking, check if the product does not exist
        # somewhere internally already Checking that a positive quant already
        # exists in an internal location is too restrictive. Indeed, if a warehouse
        # is configured with several steps (e.g. "Pick + Pack + Ship") and
        # one step is forced (creates a quant of qty = -1.0), it is not possible
        # afterwards to correct the inventory unless the product leaves the stock.
        picking_type = move.picking_id.picking_type_id if move.picking_id else False

        if (check_lot and lot_id and move.product_id.tracking == 'serial'
                and ((picking_type.use_create_lots or picking_type.use_existing_lots)
                     or not picking_type)):
            other_quants = self.search([
                ('product_id', '=', move.product_id.id),
                ('lot_id', '=', lot_id),
                ('qty', '>', 0.0),
                ('location_id.usage', '=', 'internal')])

            if other_quants:
                # We raise an error if:
                # - the total quantity is strictly larger than 1.0
                # - there are more than one negative quant,
                # to avoid situations where the user would
                # force the quantity at several steps of the process
                if (sum(other_quants.mapped('qty')) > 1.0
                        or len([q for q in other_quants.mapped('qty') if q < 0]) > 1):
                    lot_name = self.env['stock.production.lot'].browse(lot_id).name
                    raise UserError(
                        _('The serial number %s is already in stock.') % lot_name +
                        _("Otherwise make sure the right stock/owner is set."))
