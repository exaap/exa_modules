# -*- coding: utf-8 -*-
# Copyright 2020 Juan Sebastian Ocampo Ospina <Github@Capriatto>
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    is_corporate_commercial = fields.Boolean(string='Corporate Commercial?')
