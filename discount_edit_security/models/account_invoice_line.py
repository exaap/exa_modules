# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    edit_discount_account= fields.Boolean(string="Edit 'Discount Field' Field",
                                         compute='_get_edit_discount_account_field',
                                         store=False)

    @api.multi
    def _get_edit_discount_account_field(self):
        user = self.env['res.users'].search([('id', '=', self.env.user.id)])
        edit_discount_account = False

        if user.has_group('discount_edit_security.group_discount_edit'):
            edit_discount_account = True

        for line in self:
            line.edit_discount_account = edit_discount_account
