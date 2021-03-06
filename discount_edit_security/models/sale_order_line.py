# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    edit_discount_field = fields.Boolean(string="Edit 'Discount Field' Field",
                                         compute='_get_edit_discount_field',
                                         store=False)

    @api.multi
    def _get_edit_discount_field(self):
        user = self.env['res.users'].search([('id', '=', self.env.user.id)])
        edit_discount_field = False

        if user.has_group('discount_edit_security.group_discount_edit'):
            edit_discount_field = True

        for line in self:
            line.edit_discount_field = edit_discount_field
