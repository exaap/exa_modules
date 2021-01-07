# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def create(self, vals):
        template = super(ProductTemplate, self).create(vals)
        related_vals = {}
        if vals.get('default_code'):
            brand_prefix = self.env["product.brand"].search([
                ('id', '=', vals.get('product_brand_id'))
            ]).prefix
            related_vals['default_code'] = (brand_prefix or
                                            '') + ' - ' + vals['default_code']
        if related_vals:
            template.write(related_vals)
        return template

    @api.multi
    def write(self, vals):
        if vals.get('product_brand_id'):
            brand_prefix = self.env["product.brand"].search([
                ('id', '=', vals.get('product_brand_id'))
            ]).prefix
            product = self.env["product.template"].search([('id', '=', self.id)
                                                           ]).default_code
            if brand_prefix is False:
                raise UserError(_("The brand does not have a prefix assigned"))
            code = product
            prefix = code.find(brand_prefix, 0, 2)
            if prefix == 0:
                vals['default_code'] = self.default_code
            if prefix == -1:
                default_code = self.default_code
                default_code.replace('-', '')
                default_code_2 = default_code.replace('-', '')
                defaultcode2 = default_code_2[3:]
                defaultcode2.replace('-', '')
                vals['default_code'] = (brand_prefix
                                        or '') + '-' + defaultcode2

        return super(ProductTemplate, self).write(vals)