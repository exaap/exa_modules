# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    initial_position = fields.Char(string="Initial Position",
                                   help="Initial position in main winery")
    final_position = fields.Char(string="Final Position",
                                 help="Final position in main winery")
    position_product = fields.Char(string="Position in main winery",
                                   compute="_position_name")

    @api.depends('initial_position', 'final_position')
    def _position_name(self):
        for record in self:
            record.position_product = (record.initial_position
                                       or '') + '  --->  ' + (
                                           record.final_position or '')
