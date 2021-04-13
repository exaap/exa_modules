# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from odoo import fields, models


class AccountAccount(models.Model):
    _inherit = 'account.account'

    is_service_order = fields.Boolean(string='Is a Service Order Account?',
                                      defualt=False)
