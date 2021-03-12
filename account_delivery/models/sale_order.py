# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        values = {'carrier_id': self.carrier_id.id}
        res.update(values)

        return res
