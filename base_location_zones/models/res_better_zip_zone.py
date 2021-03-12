# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class ResBetterZipZone(models.Model):
    _name = "res.better.zip.zone"

    name = fields.Char(string='Zone Name', size=64)
    district_ids = fields.Many2many(comodel_name='res.better.zip.district',
                                    string='Districts',
                                    ondelete='cascade')
    zip_id = fields.Many2one(comodel_name='res.better.zip',
                             string='City/Location')

    @api.onchange('zip_id')
    def onchange_zip_id(self):
        districts_ids = self.env['res.better.zip.district'].search([
            ('zip_id', '=', self.zip_id.id)
        ])
        list_districts = [int(row) for row in districts_ids]
        self.update({'district_ids': [[6, 0, list_districts]]})
