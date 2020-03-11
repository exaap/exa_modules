# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    origin_country_id = fields.Many2one(
        string='Origin Country',
        comodel_name='res.country')
