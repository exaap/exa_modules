# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api


class AccountAccount(models.Model):
    _inherit = "account.account"

    @api.model
    def create(self, vals):
        template = super(AccountAccount, self).create(vals)
        related_vals = {}
        if vals.get("name"):
            name = vals.get("name")
            related_vals["name"] = name.upper()
        if related_vals:
            template.write(related_vals)
        return template

    @api.multi
    def write(self, vals):
        if vals.get("name"):
            name = vals.get("name")
            vals["name"] = name.upper()
        return super(AccountAccount, self).write(vals)