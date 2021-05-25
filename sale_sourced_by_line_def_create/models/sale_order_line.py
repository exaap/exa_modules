# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model
    def create(self, values):
        line = super(SaleOrderLine, self).create(values)

        if not line.warehouse_id:
            if line.order_id.warehouse_id:
                line.write({'warehouse_id': line.order_id.warehouse_id.id})

        return line
