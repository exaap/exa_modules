from odoo import models, fields, api, _


class InventoryInherit(models.Model):
    _inherit = "stock.inventory"

    product_brand_id = fields.Many2one('product.brand',
                                       string='Brand',
                                       help='Select a brand for this product')

    @api.model
    def _selection_filter(self):
        res = super(InventoryInherit, self)._selection_filter()
        res.append(('brand', _('Brand of the product')))
        return res

    @api.multi
    def action_inventory_line_tree(self):
        action = self.env.ref('stock.action_inventory_line_tree').read()[0]
        action['context'] = {
            'default_location_id': self.location_id.id,
            'default_product_id': self.product_id.id,
            'default_prod_lot_id': self.lot_id.id,
            'default_package_id': self.package_id.id,
            'default_partner_id': self.partner_id.id,
            'default_product_brand_id': self.product_brand_id.id,
            'default_inventory_id': self.id,
        }
        return action

    @api.multi
    def _get_inventory_lines_values(self):
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

        # case 0: Filter on company
        if self.company_id:
            domain += ' AND stock_quant.company_id = %s'
            args += (self.company_id.id, )

        #case 1: Filter on One owner only or One product for a specific owner
        if self.partner_id:
            domain += ' AND owner_id = %s'
            args += (self.partner_id.id, )
        #case 2: Filter on One Lot/Serial Number
        if self.lot_id:
            domain += ' AND lot_id = %s'
            args += (self.lot_id.id, )
        #case 3: Filter on One product
        if self.product_id:
            domain += ' AND product_id = %s'
            args += (self.product_id.id, )
            products_to_filter |= self.product_id
        #case 4: Filter on A Pack
        if self.package_id:
            domain += ' AND package_id = %s'
            args += (self.package_id.id, )
        #case 5: Filter on One product category + Exahausted Products
        if self.category_id:
            categ_products = Product.search([('categ_id', '=',
                                              self.category_id.id)])
            domain += ' AND product_id = ANY (%s)'
            args += (categ_products.ids, )
            products_to_filter |= categ_products

        if self.product_brand_id:
            domain += ' AND product_brand_id = %s'
            args += (self.product_brand_id.id, )

        self.env.cr.execute(
            """SELECT product_id, sum(qty) as product_qty, stock_quant.location_id, product_brand_id, lot_id as prod_lot_id, package_id, owner_id as partner_id
            FROM stock_quant
            LEFT JOIN product_product
            ON product_product.id = stock_quant.product_id
            LEFT JOIN product_template 
            ON product_product.product_tmpl_id = product_template.id
            WHERE %s
            GROUP BY product_id, stock_quant.location_id, product_brand_id, lot_id, package_id, partner_id """
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
        if self.exhausted:
            exhausted_vals = self._get_exhausted_inventory_line(
                products_to_filter, quant_products)
            vals.extend(exhausted_vals)
        return vals
