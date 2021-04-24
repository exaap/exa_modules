# -*- coding: utf-8 -*-
# Copyright 2019 EXA Auto Parts S.A.S Joan Marín <Github@joanmarin> 
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    """Adds Birth and Foundation Dates."""
    _inherit = "res.partner"

    birth_or_foundation_date = fields.Date()
    related_birth_or_foundation_date = fields.Date(
        string="Foundation Date",
        related="birth_or_foundation_date",
        store=False)
