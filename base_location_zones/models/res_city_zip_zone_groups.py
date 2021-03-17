# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class ResCityZipZoneGroups(models.Model):
    _name = "res.city.zip.zone.groups"

    name = fields.Char(string='Zone Group', size=64)
    zone_ids = fields.Many2many(comodel_name='res.city.zip.zone',
                                relation='zone_and_zonegroup_relation',
                                string='Zones',
                                ondelete='cascade')
