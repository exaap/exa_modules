# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ResCityZipDistrict(models.Model):
    _name = "res.city.zip.district"

    name = fields.Char(string='District Name', size=64)
    zip_id = fields.Many2one(comodel_name='res.city.zip',
                             string='City/Location')
    zone_id = fields.Many2one(comodel_name='res.city.zip.zone', string='Zone')

    @api.multi
    def name_get(self):
        res = []
        for district in self:
            name = district.name + ' [' + district.zip_id.name + ']'
            res.append((district.id, name))
        return res
