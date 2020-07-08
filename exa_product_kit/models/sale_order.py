# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = ['sale.order']

    order_kit_lines = fields.One2many(
        comodel_name='sale.order.kit.line',
        inverse_name='order_id',
        string='Order Kit Lines')

    @api.multi
    def action_update_product_kits(self):
        '''Create Kit products against the selling product.'''
        values = []

        if any([l.product_id.is_kit for l in self.order_line]):
            for line in self.order_line:
                if line.product_id.is_kit:
                    values.append((0, 0, {
                        'product_id': line.product_id.id,
                        'product_qty': line.product_uom_qty,
                        'price_unit': line.price_unit,
                        'discount': line.discount}))
                    line.unlink()

            self.write({'order_kit_lines': values})

        if any([l.is_product_kit for l in self.order_line]):
            for line in self.order_line:
                if line.is_product_kit:
                    line.unlink()

        values = []

        for order_kit_line in self.order_kit_lines:
            for product_kit_line in order_kit_line.product_id.product_kit_lines:
                if order_kit_line.product_qty > 0 and product_kit_line.product_qty > 0:
                    price_unit = 0

                    if product_kit_line.percent_price > 0:
                        price_unit = order_kit_line.price_unit * product_kit_line.percent_price
                        price_unit = price_unit / 100 / product_kit_line.product_qty

                    values.append((0, 0, {
                        'sequence': order_kit_line.product_id.sequence,
                        'product_id': product_kit_line.product_id.id,
                        'product_uom_qty': order_kit_line.product_qty * product_kit_line.product_qty,
                        'price_unit': price_unit,
                        'is_product_kit': True,
                        'order_kit_line_id': order_kit_line.id}))
                else:
                    raise UserError(_('Product Qty Should be greater than Zero.'))

        self.write({'order_line': values})

        return True

    @api.multi
    def action_confirm(self):
        if (any([l.product_id.is_kit for l in self.order_line])
                or any([l.is_product_kit for l in self.order_line])
                or self.order_kit_lines):
            self.action_update_product_kits()

        return super(SaleOrder, self).action_confirm()
