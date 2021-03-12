# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class ResBetterZipDistrict(models.Model):
    _name = "res.better.zip.district"

    name = fields.Char('District Name', size=64)
    zip_id = fields.Many2one(comodel_name='res.better.zip',
                             string='City/Location')
    zone_id = fields.Many2one(comodel_name='res.better.zip.zone',
                              string='Zone')

    @api.multi
    def name_get(self):
        res = []
        for district in self:
            name = district.name + ' [' + district.zip_id.city + ']'
            res.append((district.id, name))
        return res
