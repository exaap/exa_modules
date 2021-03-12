# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    def _get_stock_move_values(self):
        res = super(ProcurementRule, self)._get_stock_move_values()
        res['is_product_kit'] = self.sale_line_id.is_product_kit
        res['order_kit_line_id'] = self.sale_line_id.order_kit_line_id.id

        return res
