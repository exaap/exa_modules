# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ResBetterZipZoneGroups(models.Model):
    _name = "res.better.zip.zone.groups"

    name = fields.Char('Zone Group', size=64)
    zone_ids = fields.Many2many('res.better.zip.zone',
                                'zone_and_zonegroup_relation',
                                string='Zones',
                                ondelete='cascade')
