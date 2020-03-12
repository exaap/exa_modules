# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_manufacturer_ids = fields.One2many(
        string='Homologs',
        comodel_name='product.manufacturer',
        inverse_name='product_template_id')
