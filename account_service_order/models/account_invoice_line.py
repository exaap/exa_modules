# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from odoo import fields, models, api


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    service_order_id = fields.Many2one(comodel_name='account.service.order',
                                       string='Service Order')
    has_service_order = fields.Selection(
        related='invoice_id.has_service_order',
        string='Has Service Order?',
        store=False)
    has_more_service_orders = fields.Boolean(
        related='invoice_id.has_more_service_orders',
        string='Has more service orders?',
        store=False)

    @api.model
    def create(self, vals):
        line = super(AccountInvoiceLine, self).create(vals)

        if (line.has_service_order == 'yes'
                and not line.has_more_service_orders
                and line.service_order_id != line.invoice_id.service_order_id):
            line.service_order_id = line.invoice_id.service_order_id

        return line
