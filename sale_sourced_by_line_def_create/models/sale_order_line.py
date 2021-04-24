# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models

class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line']

    def create(self, values):
        line = super(SaleOrderLine, self).create(values)

        if not line.warehouse_id:
            if line.order_id.warehouse_id:
                line.write({'warehouse_id': line.order_id.warehouse_id.id})

        return line