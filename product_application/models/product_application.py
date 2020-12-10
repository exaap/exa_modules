# -*- coding: utf-8 -*-
from odoo import api, models, fields


class ProductApplications(models.Model):
    _name = "product.application"

    name = fields.Char(string="Product Application")
    product_application_category_ids = fields.Many2one(
        comodel_name="product.application.category", string="Category")

    child_ids = fields.One2many('product.application.category', 'parent_id',
                                'Subcategories', domain=[])

    product_ids = fields.Many2many(comodel_name="product.template",
                                   string="Products")
