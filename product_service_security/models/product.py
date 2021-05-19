# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from odoo.exceptions import UserError


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def create(self, vals):
        if vals.get("type") == "service":
            user = self.env['res.users'].search([('id', '=', self.env.user.id)
                                                 ])
            if not user.has_group('product_service_security.group_services'):
                raise UserError(
                    _("Can't create service-type products, contact your system administrator"
                      ))
        return super(ProductProduct, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get("type") == "service":
            user = self.env['res.users'].search([('id', '=', self.env.user.id)
                                                 ])
            if not user.has_group('product_service_security.group_services'):
                raise UserError(
                    _("Can't create service-type products, contact your system administrator"
                      ))
        return super(ProductProduct, self).write(vals)
