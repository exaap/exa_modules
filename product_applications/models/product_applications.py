from odoo import models, fields


class ProductApplications(models.Model):
    _name = "product.applications"

    name = fields.Char(string="Aplicacion Del Producto")
    products = fields.Many2many(comodel_name="product.template",
                                string="Productos")
