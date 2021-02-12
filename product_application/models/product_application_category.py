# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class ProductApplicationsCategory(models.Model):
    _name = 'product.application.category'
    _parent_store = True

    name = fields.Char(translate=True, required=True)

    parent_id = fields.Many2one('product.application.category',
                                'Parent Category',
                                ondelete='restrict')

    child_ids = fields.One2many('product.application.category', 'parent_id',
                                'Subcategories')

    parent_left = fields.Integer('Parent Left', index=True)

    parent_right = fields.Integer('Parent Right', index=True)
