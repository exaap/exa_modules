# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductApplications(models.Model):
    _name = "product.application"

    name = fields.Char(string="Product Application")
    product_ids = fields.Many2many(comodel_name="product.template",
                                   string="Products")

    product_application_type = fields.Many2many(
        comodel_name="product.application.type",
        string="Product application type")


class ProductApplicationsType(models.Model):
    _name = "product.application.type"

    name = fields.Char(string="Product application type")
    reference_type = fields.Integer(string="Reference")
