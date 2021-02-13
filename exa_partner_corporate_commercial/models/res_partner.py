# -*- coding: utf-8 -*-
# Copyright 2020 Juan Sebastian Ocampo Ospina <Github@Capriatto>
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_corporate_commercial = fields.Boolean(
        related='user_id.is_corporate_commercial')
