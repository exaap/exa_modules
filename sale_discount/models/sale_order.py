# -*- coding: utf-8 -*-
# Copyright 2014 Odoo 8 - M.Hagag@DVIT.ME - http://dvit.me/
# Copyright 2018 Joan Marín <Github@joanodoo>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    disc_total = fields.Float(string='Total Discount',
                              compute='_discount_total',
                              digits=dp.get_precision('Account'),
                              store=True,
                              readonly=True)

    @api.one
    @api.depends('order_line.price_unit', 'order_line.discount',
                 'order_line.product_uom_qty')
    def _discount_total(self):
        self.disc_total = sum(
            (line.product_uom_qty * line.price_unit * line.discount) / 100
            for line in self.order_line)

    total_b4_disc = fields.Float(string='Total Before The Discount',
                                 compute='_total_alls',
                                 digits=dp.get_precision('Account'),
                                 store=True,
                                 readonly=True)

    @api.one
    @api.depends('order_line.price_unit', 'order_line.product_uom_qty')
    def _total_alls(self):
        self.total_b4_disc = sum((line.product_uom_qty * line.price_unit)
                                 for line in self.order_line)
