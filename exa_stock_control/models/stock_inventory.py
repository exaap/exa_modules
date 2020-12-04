# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class InventoryInherit(models.Model):
    _inherit = "stock.inventory"

    product_brand_id = fields.Many2many(comodel_name='product.brand',
                                        string='Select Product Brand',
                                        help='select Product Brand')
    adjustment_date = fields.Datetime(string="Date of last Adjustment",
                                      required=True)

    @api.model
    def _selection_filter(self):
        res = super(InventoryInherit, self)._selection_filter()
        res.append(('brand', _('Brand of the product')))
        return res

    @api.multi
    def action_inventory_line_tree2(self):
        action = self.env.ref('stock.action_inventory_line_tree').read()[0]
        action['context'] = {
            'default_location_id': self.location_id.id,
            'default_product_id': self.product_id.id,
            'default_prod_lot_id': self.lot_id.id,
            'default_package_id': self.package_id.id,
            'default_partner_id': self.partner_id.id,
            'default_product_brand_id': self.product_brand_id.ids,
            'default_inventory_id': self.id,
        }
        return action

    @api.multi
    def _get_inventory_lines_values(self):
        if self.product_brand_id:
            # TDE CLEANME: is sql really necessary ? I don't think so
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
                        item[0] for item in product_data.items()
                        if item[1] is None
                ]:
                    product_data[void_field] = False
                product_data['theoretical_qty'] = product_data['product_qty']
                if product_data['product_id']:
                    product_data['product_uom_id'] = Product.browse(
                        product_data['product_id']).uom_id.id
                    quant_products |= Product.browse(
                        product_data['product_id'])
                vals.append(product_data)

            if self.exhausted and products_to_filter:
                exhausted_vals = self._get_exhausted_inventory_line(
                    products_to_filter, quant_products)
                vals.extend(exhausted_vals)

            if vals:
                return vals
            else:
                raise UserError(
                    _('There are no products available on the selected date %s'
                      ) % self.adjustment_date)
        else:
            return super(InventoryInherit, self)._get_inventory_lines_values()


class InventoryLine(models.Model):
    _inherit = "stock.inventory.line"

    initial_position = fields.Char(string="Initial Position",
                                   related="product_id.initial_position")
    final_position = fields.Char(string="Final Position",
                                 related="product_id.final_position")
    position = fields.Char(string="Position Product",
                           related='product_id.position_product')
    product_brand_id = fields.Many2one(string="Product brand",
                                       related="product_id.product_brand_id")
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