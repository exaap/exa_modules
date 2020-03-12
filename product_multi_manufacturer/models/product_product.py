# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        res = super(ProductProduct, self).name_search(name, args, operator, limit)
        args = args or []
        recs = []
        domain = [
            '|',
            ('manufacturer_pref', operator, name),
            ('product_manufacturer_ids', operator, name)]

        if name:
            recs = self.search(domain + args, limit=limit)
        else:
            recs = self.search(args, limit=limit)

        return res + recs.name_get()
