# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api


class ProductBrand(models.Model):
    _inherit = "product.brand"

    @api.model
    def create(self, vals):
        template = super(ProductBrand, self).create(vals)
        related_vals = {}
        if vals.get("name"):
            name = vals.get("name")
            related_vals["name"] = name.upper()
        if related_vals:
            template.write(related_vals)
        return template

    @api.multi
    def write(self, vals):
        if vals.get("name"):
            name = vals.get("name")
            vals["name"] = name.upper()
        return super(ProductBrand, self).write(vals)