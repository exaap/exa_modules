# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = ['product.template']

    sequence = fields.Integer(string='Sequence')
    is_kit = fields.Boolean(string='Is a Kit')
    product_kit_lines = fields.One2many(comodel_name='product.kit.line',
                                        inverse_name='product_tmpl_id',
                                        string='Products')

    @api.multi
    def write(self, vals):
        for product in self:
            if product.product_kit_lines:
                for line in product.product_kit_lines:
                    line.product_id.sequence = 5

            if product.type == 'service':
                vals.update({'Sequence': 1})

        return super(ProductTemplate, self).write(vals)
