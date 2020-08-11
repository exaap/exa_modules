# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp


class AccountInvoiceLine(models.Model):
    _inherit = ['account.invoice.line']

    @api.multi
    @api.depends("quantity")
    def _compute_quantity_signed(self):
        for invoice_line in self:
            quantity_signed = invoice_line.quantity

            if invoice_line.invoice_id.type in ('out_refund', 'in_refund'):
                quantity_signed *= -1

            invoice_line.quantity_signed = quantity_signed

    quantity_signed = fields.Float(
        string='Quantity Signed',
        digits=dp.get_precision('Product Unit of Measure'),
        compute="_compute_quantity_signed",
        store=True)
