# -*- coding: utf-8 -*-
# Copyright 2014 Odoo 8 - M.Hagag@DVIT.ME - http://dvit.me/
# Copyright 2018 Joan Marín <Github@joanodoo>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.addons import decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    disc_line = fields.Float(string='Discount',
                             compute='_discount_line',
                             digits=dp.get_precision('Account'),
                             store=True)

    @api.one
    @api.depends('price_unit', 'discount', 'product_uom_qty')
    def _discount_line(self):
        self.disc_line = self.price_unit * (
            (self.discount or 0.0) / 100.0) * self.product_uom_qty

    total_line = fields.Float(string='Total',
                              compute='_total_line',
                              digits=dp.get_precision('Account'),
                              store=True)

    @api.one
    @api.depends('price_unit', 'product_uom_qty')
    def _total_line(self):
        self.total_line = self.price_unit * self.product_uom_qty
