# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@joanodoo>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    editing_state_of_raws = fields.Selection([('draft', 'Draft'),
                                              ('done', 'Done')],
                                             string='Editing State of Raws',
                                             default='done')

    @api.multi
    def _generate_moves(self):
        for production in self:
            production.editing_state_of_raws = 'draft'
            production._generate_finished_moves()
            factor = production.product_uom_id._compute_quantity(
                production.product_qty, production.bom_id.product_uom_id
            ) / production.bom_id.product_qty
            boms, lines = production.bom_id.explode(
                production.product_id,
                factor,
                picking_type=production.bom_id.picking_type_id)
            production._generate_raw_moves(lines)

        return True

    @api.multi
    def action_confirm(self):
        for production in self:
            production.editing_state_of_raws = 'done'
            production._adjust_procure_method()
            production.move_raw_ids._action_confirm()
            production._generate_price_unit()

        return True

    @api.multi
    def _generate_price_unit(self):
        for production in self:
            production_cost = 0.0

            if production.routing_id:
                routing = production.routing_id
            else:
                routing = production.bom_id.routing_id

            if routing and routing.location_id:
                source_location = routing.location_id
            else:
                source_location = production.location_src_id

            for move_raw in production.move_raw_ids:
                move_raw.write({
                    'origin':
                    production.name,
                    'price_unit':
                    move_raw.product_id.standard_price,
                    'name':
                    production.name,
                    'propagate':
                    False,
                    'group_id':
                    production.procurement_group_id
                    and production.procurement_group_id.id or False,
                    'location_dest_id':
                    move_raw.product_id.property_stock_production.id,
                    'unit_factor':
                    move_raw.product_uom_qty / production.product_qty or 0.0,
                    'quantity_done_store':
                    False
                })

                production_cost += move_raw.price_unit * move_raw.product_uom_qty

            for move_finished in production.move_finished_ids:
                move_finished.price_unit = production_cost / production.product_qty

        return True