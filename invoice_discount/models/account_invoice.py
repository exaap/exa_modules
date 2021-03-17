# -*- coding: utf-8 -*-
# Copyright 2014 Odoo 8 - M.Hagag@DVIT.ME - http://dvit.me/
# Copyright 2018 Joan Marín <Github@JoanMarin>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
from odoo.addons import decimal_precision as dp


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    disc_total = fields.Float(string='Total Discount',
                              compute='_discount_total',
                              digits=dp.get_precision('Account'),
                              store=True,
                              readonly=True)

    @api.multi
    @api.depends('invoice_line_ids.price_unit', 'invoice_line_ids.discount',
                 'invoice_line_ids.quantity')
    def _discount_total(self):
        self.disc_total = sum(
            (line.quantity * line.price_unit * line.discount) / 100
            for line in self.invoice_line_ids)

    total_b4_disc = fields.Float(string='Total Before The Discount',
                                 compute='_total_alls',
                                 digits=dp.get_precision('Account'),
                                 store=True,
                                 readonly=True)

    @api.multi
    @api.depends('invoice_line_ids.price_unit', 'invoice_line_ids.quantity')
    def _total_alls(self):
        self.total_b4_disc = sum((line.quantity * line.price_unit)
                                 for line in self.invoice_line_ids)
