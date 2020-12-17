# -*- coding: utf-8 -*-
# Copyright 2020 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class ResSettings(models.Model):
    _inherit = 'res.config.settings'

    email_exceptions_ids = fields.Many2many(
        comodel_name="res.partner.email.exception")
