# -*- coding: utf-8 -*-
# Copyright 2020 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    def toggle_active(self):
        user = self.env['res.users'].search([('id', '=', self.env.user.id)])
        if not user.has_group('product_application.group_archive'):
            raise UserError(_('You cannot archive products'))
        return super(ResPartner, self).toggle_active()