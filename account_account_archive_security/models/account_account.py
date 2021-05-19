# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountAccount(models.Model):
    _inherit = "account.account"

    active = fields.Boolean(default=True)

    @api.multi
    def toggle_active(self):
        user = self.env['res.users'].search([('id', '=', self.env.user.id)])
        if not user.has_group('account.group_account_manager'):
            raise UserError(_('You cannot archive Accounts'))
        return super(AccountAccount, self).toggle_active()
