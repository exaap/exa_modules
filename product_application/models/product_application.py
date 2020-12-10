# -*- coding: utf-8 -*-
# Copyright 2020 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class ProductApplications(models.Model):
    _name = "product.application"

    name = fields.Char(string="Product Application")
    application_category_id = fields.Many2one(
        comodel_name="product.application.category",
        string="Category",
        domain=[('parent_id', '=', False)])
    application_line_id = fields.Many2one(
        comodel_name="product.application.category", string="Line")
    application_subline_id = fields.Many2one(
        comodel_name="product.application.category", string="Subline")
    product_ids = fields.Many2many(comodel_name="product.template",
                                   string="Products")
