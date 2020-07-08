# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductKitLine(models.Model):
    _name = 'product.kit.line'
    _description = "Product Kit Lines"

    product_id = fields.Many2one(comodel_name='product.product', string='Product')
    product_tmpl_id = fields.Many2one(
        comodel_name='product.template',
        string='Product Template')
    product_qty = fields.Float(string='Quantity')
    sequence = fields.Integer(string='Sequence')
    percent_price = fields.Float(
        string='Percentage Price (%)',
        help='Percentage from 0 to 100 regarding the price of the Kit.',
        default=0.00)
