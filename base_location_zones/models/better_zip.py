# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class BetterZip(models.Model):
    _inherit = 'res.better.zip'

    zone_ids = fields.One2many('res.better.zip.zone', 'zip_id', string='Zone')
