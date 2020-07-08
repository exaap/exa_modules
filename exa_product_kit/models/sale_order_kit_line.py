# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
import odoo.addons.decimal_precision as dp


class SaleOrderKitLine(models.Model):
    _name = 'sale.order.kit.line'
    _description = "Sale Order Kit Lines"

    name = fields.Char(store=False, compute='name_get')
    order_id = fields.Many2one(comodel_name='sale.order', string='Order')
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product Kit',
        domain=[('is_kit', '=', True)])
    product_qty = fields.Float('Quantity')
    price_unit = fields.Float(
        string='Price Unit',
        digits=dp.get_precision('Product Price'))
    discount = fields.Float(
        string='Discount',
        default=0.00)

    def name_get(self):
        res = []

        for record in self:
            name = u'(%s) [%s] %s (%s)' % (
                record.order_id.name or '',
                record.product_id.default_code or '',
                record.product_id.name or '',
                record.product_qty)
            res.append((record.id, name))

        return res
