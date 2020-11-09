from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    apllications = fields.Many2many(comodel_name="product.applications",
                                    string="Aplicacion del Producto")
