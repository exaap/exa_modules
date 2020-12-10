# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_apllication_ids = fields.Many2many(
        comodel_name="product.application",
        string="Product Application",
        required=True)
    product_application_category_ids = fields.Many2one(
        comodel_name="product.application",
        related="product_apllication_ids.product_application_category_ids")
    child_ids = fields.One2many(comodel_name="product.application",
                                related="product_apllication_ids.child_ids")
