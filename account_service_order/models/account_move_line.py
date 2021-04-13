# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    has_service_order = fields.Selection(selection=[('no', 'No'),
                                                    ('yes', 'Yes')],
                                         string='Has Service Order?',
                                         default=False)
    service_order_id = fields.Many2one(comodel_name='account.service.order',
                                       string='Service Order')
    is_service_order_account = fields.Boolean(
        related='account_id.is_service_order',
        string='Is a Service Order Account?',
        store=False)
    account_journal_type = fields.Selection(related='move_id.journal_id.type',
                                            string='Journal Type',
                                            store=False)
