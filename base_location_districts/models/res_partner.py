# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    district_id = fields.Many2one(comodel_name='res.city.zip.district',
                                  string='District')

    @api.onchange('district_id')
    def onchange_district(self):
        if self.district_id:
            self.zip_id = self.district_id.zip_id
