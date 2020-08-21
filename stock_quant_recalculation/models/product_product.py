# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime
from odoo import api, models, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare

LOGGER = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.multi
    def _moves_assigned(self):
        return self.env['stock.move'].search([
            ('state', '=', 'assigned'),
            ('product_id', '=', self.id)])

    @api.multi
    def _moves_waiting(self):
        return self.env['stock.move'].search([
            ('state', '=', 'waiting'),
            ('product_id', '=', self.id)])

    @api.multi
    def recalculate_quants(self):
        initial_datetime = datetime.now()

        msg1 = _('Has stock moves in assigned state.')
        msg2 = _('Has stock moves in waiting state.')

        if self._moves_assigned():
            raise UserError(msg1)

        if self._moves_waiting():
            raise UserError(msg2)

        Quant = self.env['stock.quant']
        move_count = 0
        diff_dates = False

        if not self.quants_recalculated:
            self.stock_quant_ids.with_context(force_unlink=True).unlink()
            moves = self.env['stock.move'].search(
                [('state', '=', 'done'), ('product_id', '=', self.id)],
                order='date asc')

            for move in moves:
                # In case no pack operations in picking
                if float_compare(
                        move.product_qty,
                        0,
                        precision_rounding=move.product_id.uom_id.rounding) > 0:
                    move.check_tracking(False)  # TDE: do in batch ? redone ? check this
                    preferred_domain_list = [
                        [('reservation_id', '=', move.id)],
                        [('reservation_id', '=', False)],
                        ['&',
                         ('reservation_id', '!=', move.id),
                         ('reservation_id', '!=', False)]]
                    quants = Quant.quants_get_preferred_domain(
                        move.product_qty,
                        move,
                        domain=[('qty', '>', 0)],
                        preferred_domain_list=preferred_domain_list)
                    Quant.quants_move_recalculation(
                        quants,
                        move,
                        move.location_dest_id,
                        lot_id=move.restrict_lot_id.id,
                        owner_id=move.restrict_partner_id.id)

                move_count += 1
                diff_dates = datetime.now() - initial_datetime
                LOGGER.info(
                    "---Quants Recalculate-->Seconds: %s, Moves: %s, %s(%s)---",
                    diff_dates.total_seconds(),
                    move_count,
                    self.default_code,
                    self.id)

            self.write({
                'quants_recalculated': True,
                'last_date_quants_recalculated': initial_datetime})

        return True
