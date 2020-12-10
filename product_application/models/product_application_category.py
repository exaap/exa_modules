from odoo import models, fields


class ProductApplicationsCategory(models.Model):
    _name = 'product.application.category'
    _parent_store = True

    name = fields.Char(translate=True, required=True)

    parent_id = fields.Many2one('product.application.category',
                                'Parent Category',
                                ondelete='restrict')
    parent_path = fields.Char(index=True)

    parent_left = fields.Integer('Parent Left', index=True)

    parent_right = fields.Integer('Parent Right', index=True)

    child_ids = fields.One2many('product.application.category', 'parent_id',
                                'Subcategories')
