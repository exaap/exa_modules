# -*- coding: utf-8 -*-
# Copyright 2018 Humanitarian Logistics Organisation e.V. - Stefan Becker
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResPartner(models.Model):
    """Add social media fields"""
    _inherit = "res.partner"

    youtube = fields.Char()
    instagram = fields.Char()
    whatsapp = fields.Char()
    telegram = fields.Char()