# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    zone_id = fields.Many2one(comodel_name='res.city.zip.zone', string='Zone')
    zone_group_id = fields.Many2one(compute='_compute_zone_group',
                                    comodel_name='res.city.zip.zone.groups',
                                    string="Zone Group",
                                    store=True)

    @api.depends('zone_id')
    @api.one
    def _compute_zone_group(self):
        if self.zone_id:
            zone_group_ids = self.env['res.city.zip.zone.groups'].search([
                ('zone_ids', 'in', self.zone_id.ids)
            ])
            if zone_group_ids:
                for zone in zone_group_ids:
                    self.zone_group_id = zone.id

    @api.onchange('district_id')
    def onchange_district(self):
        if self.district_id:
            self.zone_id = self.district_id.zone_id
        else:
            self.zone_id = ''
        return super(ResPartner, self).onchange_district()

    @api.onchange('zip_id')
    def _onchange_zip_id(self):
        res = super(ResPartner, self)._onchange_zip_id()
        if self.zip_id:
            for rec in self.zip_id.zone_ids:
                self.zone_id = rec
                break
        else:
            self.zone_id = ''
        return res
