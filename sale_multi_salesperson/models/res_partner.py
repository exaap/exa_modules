# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    multi_user_ids = fields.Many2many(comodel_name='res.users',string='Other Salespersons')

    @api.model
    def create(self, vals):
        res = super(ResPartner, self).create(vals)

        if res.multi_user_ids:
            res.message_subscribe_users(user_ids=res.multi_user_ids.ids)

        if res.user_id:
            res.message_subscribe_users(user_ids=[res.user_id.id])

        return res

    @api.multi
    def write(self, vals):
        if vals.get('user_id'):
            self.message_subscribe_users(user_ids=[vals['user_id']])

        if vals.get('multi_user_ids'):
            self.message_subscribe_users(user_ids=vals['multi_user_ids'][0][2])

        return super(ResPartner, self).write(vals)
