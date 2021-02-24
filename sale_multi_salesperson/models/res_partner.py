# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    multi_user_ids = fields.Many2many(
        comodel_name='res.users',
        string='Other Salespersons')

    @api.model
    def create(self, vals):
        rec = super(ResPartner, self).create(vals)

        if rec.multi_user_ids:
            rec.message_subscribe(
                partner_ids=rec.multi_user_ids.mapped('partner_id').ids)

        if rec.user_id:
            rec.message_subscribe(
                partner_ids=rec.user_id.mapped('partner_id').ids)

        return rec

    @api.multi
    def write(self, vals):
        res = super(ResPartner, self).write(vals)

        for partner in self:
            if vals.get('multi_user_ids'):
                partner.message_subscribe(
                    partner_ids=partner.multi_user_ids.mapped('partner_id').ids)

            if vals.get('user_id'):
                partner.message_subscribe(
                    partner_ids=partner.user_id.mapped('partner_id').ids)

        return res
