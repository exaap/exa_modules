from odoo import models, fields


class ProductApplications(models.Model):
    _name = "product.application"

    name = fields.Char(string="Product Application")
    product_ids = fields.Many2many(comodel_name="product.template",
                                   string="Products")
