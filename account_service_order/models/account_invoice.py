# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from odoo import fields, models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def _compute_move_lines(self):
        for invoice in self:
            move_line_ids = []
            service_orders = []

            for line in invoice.invoice_line_ids:
                if line.service_order_id:
                    if line.service_order_id not in service_orders:
                        service_orders.append(line.service_order_id)

            for service_order in service_orders:
                for move_line in service_order.move_lines:
                    move_line_ids.append(move_line.id)

            move_lines = self.env['account.move.line'].browse(move_line_ids)
            invoice.service_order_move_lines = move_lines

    @api.onchange('service_order_id', 'has_service_order',
                  'has_more_service_orders')
    def _onchange_service_order(self):
        for invoice in self:
            if (not invoice.has_more_service_orders
                    and invoice.has_service_order == 'yes'
                    and invoice.service_order_id):
                for line in invoice.invoice_line_ids:
                    if line.service_order_id != invoice.service_order_id:
                        line.service_order_id = invoice.service_order_id
            elif invoice.has_more_service_orders:
                if invoice.has_service_order != 'yes':
                    invoice.has_service_order = 'yes'

                for line in invoice.invoice_line_ids:
                    if line.service_order_id:
                        line.service_order_id = False
            else:
                for line in invoice.invoice_line_ids:
                    if line.service_order_id:
                        line.service_order_id = False

    has_service_order = fields.Selection([('no', 'No'), ('yes', 'Yes')],
                                         string='Has Service Order?',
                                         index=True,
                                         change_default=True,
                                         track_visibility='always')
    service_order_id = fields.Many2one('account.service.order',
                                       string='Service Order')
    has_more_service_orders = fields.Boolean(string='Has more service orders?')
    service_order_move_lines = fields.One2many(
        comodel_name='account.move.line',
        string='Journal Items',
        compute='_compute_move_lines')
