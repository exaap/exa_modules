# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class StockMove(models.Model):
    _inherit = ['stock.move']

    is_product_kit = fields.Boolean(string='Part of a Product Kit?',
                                    readonly=True,
                                    default=False)
    order_kit_line_id = fields.Many2one(comodel_name='sale.order.kit.line',
                                        string='Order Kit Line')
