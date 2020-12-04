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

    edit_position_fields = fields.Boolean(
        string="Edit 'Positions Fields' Field",
        compute='_get_edit_positions_fields',
        store=False)

    @api.depends('initial_position', 'final_position')
    def _position_name(self):
        for record in self:
            record.position_product = (record.initial_position
                                       or '') + '  --->  ' + (
                                           record.final_position or '')

    @api.multi
    def _get_edit_positions_fields(self):
        user = self.env['res.users'].search([('id', '=', self.env.user.id)])
        edit_position_fields = False

        if user.has_group(
                'exa_stock_control.exa_stock_control_group_manager_position'):
            edit_position_fields = True

        for products in self:
            products.edit_position_fields = edit_position_fields
