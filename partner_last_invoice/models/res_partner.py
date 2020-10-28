# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    last_out_invoice_id = fields.Many2one(
        comodel_name='account.invoice',
        string="Last Customer Invoice",
        readonly=True,
        compute="_compute_last_invoice",
        copy=False,
        store=True)
    last_out_invoice_amount = fields.Monetary(
        string="Last Customer Invoice Amount",
        readonly=True,
        compute="_compute_last_invoice",
        copy=False,
        store=True)
    last_out_invoice_date = fields.Date(
        string="Last Customer Invoice Date",
        readonly=True,
        compute="_compute_last_invoice",
        copy=False,
        store=True)
    last_in_invoice_id = fields.Many2one(
        comodel_name='account.invoice',
        string="Last Supplier Invoice",
        readonly=True,
        compute="_compute_last_invoice",
        copy=False,
        store=True)
    last_in_invoice_amount = fields.Monetary(
        string="Last Supplier Invoice Amount",
        readonly=True,
        compute="_compute_last_invoice",
        copy=False,
        store=True)
    last_in_invoice_date = fields.Date(
        string="Last Supplier Invoice Date",
        readonly=True,
        compute="_compute_last_invoice",
        copy=False,
        store=True)

    @api.multi
    def _compute_last_invoice(self):
        for partner in self:
            out_invoice_ids = self.env['account.invoice'].search([
                ('partner_id', '=', partner.id),
                ('type', '=', 'out_invoice'),
                ('state', 'not in', ['draft', 'cancel'])])
            out_invoice = out_invoice_ids and max(out_invoice_ids)
            in_invoice_ids = self.env['account.invoice'].search([
                ('partner_id', '=', partner.id),
                ('type', '=', 'in_invoice'),
                ('state', 'not in', ['draft', 'cancel'])])
            in_invoice = in_invoice_ids and max(in_invoice_ids)

            if out_invoice:
                partner.last_out_invoice_id = out_invoice.id
                partner.last_out_invoice_amount = out_invoice.amount_total
                partner.last_out_invoice_date = out_invoice.date_invoice

            if in_invoice:
                partner.last_in_invoice_id = in_invoice.id
                partner.last_in_invoice_amount = in_invoice.amount_total
                partner.last_in_invoice_date = in_invoice.date_invoice
