# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class StockInventoryLine(models.Model):
    _inherit = "stock.inventory.line"

    initial_position = fields.Char(string="Initial Position",
                                   related="product_id.initial_position")
    final_position = fields.Char(string="Final Position",
                                 related="product_id.final_position")
    position = fields.Char(string="Position Product",
                           related='product_id.position_product')
    product_brand_id = fields.Many2one(string="Product brand",
                                       related="product_id.product_brand_id")
    barcode = fields.Char(string="Barcode", related="product_id.barcode")
    edit_position_fields = fields.Boolean(
        string="Edit 'Positions Fields' Field",
        compute='_get_edit_positions_fields',
        store=False)

    @api.multi
    def _get_edit_positions_fields(self):
        user = self.env['res.users'].search([('id', '=', self.env.user.id)])
        edit_position_fields = False

        if user.has_group(
                'exa_stock_control.exa_stock_control_group_manager_position'):
            edit_position_fields = True

        for products in self:
            products.edit_position_fields = edit_position_fields
