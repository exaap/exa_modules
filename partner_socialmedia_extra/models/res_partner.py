# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

class ResPartner(models.Model):
    """Add social media fields"""
    _inherit = "res.partner"

    youtube = fields.Char()
    instagram = fields.Char()
    whatsapp = fields.Char()
    telegram = fields.Char()