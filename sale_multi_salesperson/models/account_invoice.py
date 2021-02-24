# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    multi_user_ids = fields.Many2many(
        comodel_name='res.users',
        string='Other Salespersons')

    @api.model
    def create(self, vals):
        rec = super(AccountInvoice, self).create(vals)

        if rec.multi_user_ids:
            rec.message_subscribe(
                partner_ids=rec.multi_user_ids.mapped('partner_id').ids)

        return rec

    @api.multi
    def write(self, vals):
        res = super(AccountInvoice, self).write(vals)

        if vals.get('multi_user_ids'):
            for invoice in self:
                invoice.message_subscribe(
                    partner_ids=invoice.multi_user_ids.mapped('partner_id').ids)

        return res

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        """
        Update the multi_user_ids fields when the partner is changed:
        """
        super(AccountInvoice, self)._onchange_partner_id()

        if self.partner_id:
            self.multi_user_ids = [(6, 0, self.partner_id.multi_user_ids.ids)]
            self.user_id = self.partner_id.user_id.id
