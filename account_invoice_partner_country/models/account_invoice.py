# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    partner_country = fields.Many2one(comodel_name="res.country",
                                      related="partner_id.country_id")
