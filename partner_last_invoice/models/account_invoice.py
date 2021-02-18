# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def _set_last_invoice(self):
        if self.type == 'out_invoice':
            out_invoice_ids = self.env['account.invoice'].search([
                ('partner_id', '=', self.partner_id.id),
                ('type', '=', 'out_invoice'),
                ('state', 'not in', ['draft', 'cancel'])
            ])
            out_invoice = out_invoice_ids and max(out_invoice_ids)

            if out_invoice:
                self.partner_id.write({
                    'last_out_invoice_id':
                    out_invoice.id,
                    'last_out_invoice_amount':
                    out_invoice.amount_total,
                    'last_out_invoice_date':
                    out_invoice.date_invoice
                })

        if self.type == 'in_invoice':
            in_invoice_ids = self.env['account.invoice'].search([
                ('partner_id', '=', self.partner_id.id),
                ('type', '=', 'in_invoice'),
                ('state', 'not in', ['draft', 'cancel'])
            ])
            in_invoice = in_invoice_ids and max(in_invoice_ids)

            if in_invoice:
                self.partner_id.write({
                    'last_in_invoice_id':
                    in_invoice.id,
                    'last_in_invoice_amount':
                    in_invoice.amount_total,
                    'last_in_invoice_date':
                    in_invoice.date_invoice
                })

    @api.multi
    def invoice_validate(self):
        res = super(AccountInvoice, self).invoice_validate()

        for invoice in self:
            invoice._set_last_invoice()

        return res

    @api.multi
    def action_cancel(self):
        res = super(AccountInvoice, self).action_cancel()

        for invoice in self:
            invoice._set_last_invoice()

        return res
