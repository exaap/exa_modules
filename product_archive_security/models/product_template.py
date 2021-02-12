# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    def toggle_active(self):
        user = self.env['res.users'].search([('id', '=', self.env.user.id)])
        if not user.has_group('product_archive_security.group_archive'):
            raise UserError(_('You cannot archive products'))
        return super(ProductTemplate, self).toggle_active()
