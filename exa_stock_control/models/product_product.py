from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.product"

    position_product = fields.Char(string="Position Product")
