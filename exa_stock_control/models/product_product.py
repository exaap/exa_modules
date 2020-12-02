# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.product"

    initial_position = fields.Char(string="Initial Position",
                                   related="product_tmpl_id.initial_position")
    final_position = fields.Char(string="Final Position",
                                 related="product_tmpl_id.final_position")
    position_product = fields.Char(string="Position Product",
                                   related="product_tmpl_id.position_product")
    brand = fields.Many2one(string="Product brand",
                            related="product_tmpl_id.product_brand_id")
