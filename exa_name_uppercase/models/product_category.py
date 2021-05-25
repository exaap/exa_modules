# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api


class ProductCategory(models.Model):
    _inherit = "product.category"

    @api.model
    def create(self, vals):
        template = super(ProductCategory, self).create(vals)
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
        return super(ProductCategory, self).write(vals)
