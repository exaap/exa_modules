# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line']

    is_product_kit = fields.Boolean(string='Part of a Product Kit?',
                                    readonly=True,
                                    default=False)
    order_kit_line_id = fields.Many2one(comodel_name='sale.order.kit.line',
                                        string='Order Kit Line')

    @api.model
    def create(self, vals):
        sequence = 10

        if vals.get('order_id') and not vals.get('sequence'):
            self._cr.execute(
                """SELECT MAX(sequence) FROM sale_order_line WHERE order_id = %s""",
                (vals.get('order_id'), ))
            res = self._cr.fetchone()

            if res and res[0]:
                if res[0] % 10 != 0:
                    rem = res[0] % 10
                    vals['sequence'] = (res[0] - rem) + 10
                else:
                    vals['sequence'] = res[0] + 10
            else:
                vals['sequence'] = sequence

        return super(SaleOrderLine, self).create(vals)

    @api.multi
    def _prepare_invoice_line(self, qty):
        res = {}
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)

        if res:
            res.update({
                'is_product_kit': self.is_product_kit,
                'order_kit_line_id': self.order_kit_line_id.id
            })

        return res
