# -*- coding: utf-8 -*-
# Copyright 2014 Odoo 8 - M.Hagag@DVIT.ME - http://dvit.me/ 
# Copyright 2018 Joan Marín <Github@joanodoo> 
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models
import odoo.addons.decimal_precision as dp

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    disc_amount = fields.Float(
        string = 'Discount',
        compute = '_discount_line',
        digits = dp.get_precision('Account'),
        store = True)

    @api.one
    @api.depends('price_unit', 'discount', 'quantity')
    def _discount_line(self):
        self.disc_amount = self.price_unit * ((self.discount or 0.0)/100.0) * self.quantity

    total_wo_disc = fields.Float(
        string = 'Total',
        compute = '_total_line',
        digits = dp.get_precision('Account'),
        store = True)

    @api.one
    @api.depends('price_unit', 'quantity')
    def _total_line(self):
        self.total_wo_disc = self.price_unit * self.quantity