# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    def _get_stock_move_values(self):
        res = super(ProcurementOrder, self)._get_stock_move_values()
        res['is_product_kit'] = self.sale_line_id.is_product_kit
        res['order_kit_line_id'] = self.sale_line_id.order_kit_line_id.id

        return res
