# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@joanmarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def action_open_quants_main_locations_variant(self):
        action = self.env.ref('stock.product_open_quants').read()[0]
        action['domain'] = [('product_id', 'in', self.ids),
                            ('location_id.usage', '=', 'internal'),
                            ('location_id.is_main', '=', True)]
        action['context'] = {
            'search_default_locationgroup': 1,
            'search_default_internal_loc': 1
        }

        return action
