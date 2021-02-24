# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    multi_user_ids = fields.Many2many(comodel_name='res.users', string='Other Salespersons')

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)

        if res.multi_user_ids:
            res.message_subscribe_users(user_ids=res.multi_user_ids.ids)

        return res

    @api.multi
    def write(self, vals):
        if vals.get('multi_user_ids'):
            self.message_subscribe_users(user_ids=vals['multi_user_ids'][0][2])

        return super(SaleOrder, self).write(vals)

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Update the multi_user_ids fields when the partner is changed:
        """
        super(SaleOrder, self).onchange_partner_id()

        if self.partner_id:
            self.multi_user_ids = [(6, 0, self.partner_id.multi_user_ids.ids)]
            self.user_id = self.partner_id.user_id.id

    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()

        if self.multi_user_ids:
            invoice_vals.update({'multi_user_ids': [(6, 0, self.multi_user_ids.ids)]})

        return invoice_vals
