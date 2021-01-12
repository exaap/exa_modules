# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    brand_prefix = fields.Char()

    @api.model
    def create(self, vals):
        template = super(ProductTemplate, self).create(vals)
        related_vals = {}
        if vals.get('default_code'):
            brand_prefix = self.env["product.brand"].search([
                ('id', '=', vals.get('product_brand_id'))
            ]).prefix
            related_vals['default_code'] = (brand_prefix
                                            or '') + vals['default_code']
            related_vals['brand_prefix'] = brand_prefix
        if related_vals:
            template.write(related_vals)
        return template

    @api.multi
    def write(self, vals):
        if vals.get("product_brand_id"):
            brand_prefix = self.env["product.brand"].search([
                ('id', '=', vals.get("product_brand_id"))
            ])
            product = self.env["product.template"].search([('id', '=', self.id)
                                                           ])
            if self.product_brand_id.prefix is False:
                raise UserError(_("The brand does not have a prefix assigned"))
            code = product.default_code
            prefix_code = product.brand_prefix
            brand_prefix_code = ""
            if prefix_code is False:
                brand_prefix_code = (brand_prefix.prefix
                                     or '') + self.default_code
                vals["brand_prefix"] = brand_prefix.prefix
            else:
                prefix = code.find(prefix_code)
                if prefix >= 0:
                    default_code = self.default_code
                    defaultcode2 = default_code[3:]
                    brand_prefix_code = (brand_prefix.prefix
                                         or '') + defaultcode2
                    vals["brand_prefix"] = brand_prefix.prefix

            vals['default_code'] = brand_prefix_code

        return super(ProductTemplate, self).write(vals)