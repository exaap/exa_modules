# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResCityZip(models.Model):
    _inherit = 'res.city.zip'

    zone_ids = fields.One2many(comodel_name='res.city.zip.zone',
                               inverse_name='zip_id',
                               string='Zone')
