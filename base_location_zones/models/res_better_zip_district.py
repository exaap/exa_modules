# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class ResBetterZipDistrict(models.Model):
    _inherit = 'res.better.zip.district'

    zone_id = fields.Many2one(comodel_name='res.better.zip.zone',
                              string='Zone')
