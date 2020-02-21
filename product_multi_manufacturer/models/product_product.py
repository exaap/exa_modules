# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100):
        res = super(ProductProduct, self).name_search(
            cr,
            user,
            name,
            args,
            operator,
            context,
            limit)
        args = args or []
        ids = False
        domain = [
            '|',
            ('manufacturer_pref', operator, name),
            ('product_manufacturer_ids', operator, name)]

        ids = False

        if name:
            ids = self.search(cr, user, domain + args, limit=limit, context=context)
        else:
            ids = self.search(cr, user, args, limit=limit, context=context)

        result = self.name_get(cr, user, ids, context=context)

        return res + result
