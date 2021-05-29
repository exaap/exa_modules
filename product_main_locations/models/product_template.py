# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@joanmarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.addons import decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    qty_avl_main_locations = fields.Float(
        string='Stock of Main Locations',
        compute='_compute_quantities_main_locations',
        digits=dp.get_precision('Product Unit of Measure'))

    @api.multi
    def _compute_quantities_main_locations(self):
        for product in self:
            qty_avl_main_locations = 0.0
            products = product.mapped('product_variant_ids')
            stock_quant_ids = self.env['stock.quant'].search([
                ('product_id', 'in', products.ids),
                ('location_id.usage', '=', 'internal'),
                ('location_id.is_main', '=', True)
            ])

            for stock_quant_id in stock_quant_ids:
                qty_avl_main_locations += stock_quant_id.quantity

            product.qty_avl_main_locations = qty_avl_main_locations

    @api.multi
    def action_open_quants_main_locations(self):
        products = self.mapped('product_variant_ids')
        action = self.env.ref('stock.product_open_quants').read()[0]
        action['domain'] = [('product_id', 'in', products.ids),
                            ('location_id.usage', '=', 'internal'),
                            ('location_id.is_main', '=', True)]
        action['context'] = {
            'search_default_locationgroup': 1,
            'search_default_internal_loc': 1
        }

        return action
