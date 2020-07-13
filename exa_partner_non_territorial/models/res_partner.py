# -*- coding: utf-8 -*-
# Copyright 2019 EXA Auto Parts S.A.S Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    """Adds Non Territorial Boolean Field."""
    _inherit = "res.partner"

    is_non_territorial = fields.Boolean(
        string="Is Non-territorial?",
        default=False)
