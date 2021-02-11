# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from datetime import datetime
from odoo import models, fields, api, _


class StockInventory(models.Model):
    _inherit = "stock.inventory"

    product_brand_id = fields.Many2many(comodel_name='product.brand',
                                        string='Select Product Brand',
                                        help='select Product Brand')
    adjustment_date = fields.Datetime(string="Date of last Adjustment")

    @api.model
    def _selection_filter(self):
        res = super(StockInventory, self)._selection_filter()
        res.append(('brand', _('Brand of the product')))
        return res

    @api.multi
    def _get_inventory_lines_values(self):
        locations = self.env['stock.location'].search([
            ('id', 'child_of', [self.location_id.id])
        ])
        domain = ' stock_quant.location_id in %s AND product_product.active = TRUE'
        args = (tuple(locations.ids), )

        vals = []
        Product = self.env['product.product']
        # Empty recordset of products available in stock_quants
        quant_products = self.env['product.product']
        # Empty recordset of products to filter
        products_to_filter = self.env['product.product']
        if self.product_brand_id:
            brand_products = Product.search([('product_brand_id', 'in',
                                              self.product_brand_id.ids)])
            domain += ' AND product_id = ANY (%s)'
            inventory_lines = self.env["stock.inventory.line"].search([
                '&', '&', ('inventory_id.date', '>', self.adjustment_date),
                ('inventory_id.state', '=', 'done'),
                ('product_id', 'in', brand_products.ids)
            ])
            adjustment_products = []

            for inventory_line in inventory_lines:
                adjustment_products.append(inventory_line.product_id.id)

            brand_products = Product.search([
                '&', ('id', 'not in', adjustment_products),
                ('product_brand_id', 'in', self.product_brand_id.ids)
            ])
            products_to_filter |= brand_products
            args += (brand_products.ids, )

        if self.filter == 'none':
            all_products = Product.search([('active', '=', True)])
            domain += ' AND product_id = ANY (%s)'
            inventory_lines = self.env["stock.inventory.line"].search([
                '&', '&', ('inventory_id.date', '>', self.adjustment_date),
                ('inventory_id.state', '=', 'done'),
                ('product_id', 'in', all_products.ids)
            ])
            adjustment_products = []

            for inventory_line in inventory_lines:
                adjustment_products.append(inventory_line.product_id.id)

            all_products = Product.search([('id', 'not in',
                                            adjustment_products)])
            products_to_filter |= all_products
            args += (all_products.ids, )

        if self.category_id:
            categ_products = Product.search([('categ_id', '=',
                                              self.category_id.id)])
            domain += ' AND product_id = ANY (%s)'
            inventory_lines = self.env["stock.inventory.line"].search([
                '&', '&', ('inventory_id.date', '>', self.adjustment_date),
                ('inventory_id.state', '=', 'done'),
                ('product_id', 'in', categ_products.ids)
            ])
            adjustment_products = []

            for inventory_line in inventory_lines:
                adjustment_products.append(inventory_line.product_id.id)

            categ_products_all = Product.search([
                '&', ('categ_id', '=', self.category_id.id),
                ('id', 'not in', adjustment_products)
            ])

            products_to_filter |= categ_products_all
            args += (categ_products_all.ids, )
        if self.product_id:
            domain += ' AND product_id = %s'
            args += (self.product_id.id, )
            products_to_filter |= self.product_id
        if self.partner_id:
            domain += ' AND owner_id = %s'
            args += (self.partner_id.id, )

        self.env.cr.execute(
            """SELECT product_id, sum(qty) as product_qty, stock_quant.location_id, lot_id as prod_lot_id, package_id, owner_id as partner_id 
                FROM stock_quant 
                LEFT JOIN product_product 
                ON product_product.id = stock_quant.product_id 
                LEFT JOIN product_template 
                ON product_product.product_tmpl_id = product_template.id 
                WHERE %s 
                GROUP BY product_id, stock_quant.location_id, lot_id, package_id, partner_id """
            % domain, args)

        for product_data in self.env.cr.dictfetchall():
            # replace the None the dictionary by False, because falsy values are tested later on
            for void_field in [
                    item[0] for item in product_data.items() if item[1] is None
            ]:
                product_data[void_field] = False
            product_data['theoretical_qty'] = product_data['product_qty']
            if product_data['product_id']:
                product_data['product_uom_id'] = Product.browse(
                    product_data['product_id']).uom_id.id
                quant_products |= Product.browse(product_data['product_id'])
            vals.append(product_data)
        if self.exhausted and products_to_filter:
            exhausted_vals = self._get_exhausted_inventory_line(
                products_to_filter, quant_products)
            vals.extend(exhausted_vals)
        if vals:
            return vals
        else:
            return super(StockInventory, self)._get_inventory_lines_values()
