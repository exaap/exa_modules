# -*- coding: utf-8 -*-
# Copyright 2021 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    @api.multi
    def set_default_acquirer(self):
        for wizard in self:
            ir_values = self.env['ir.values']
            if self.user_has_groups('exa_base.group_erp_manager'):
                ir_values = ir_values.sudo()
            ir_values.set_default(
                'payment.transaction',
                'acquirer_id',
                wizard.default_acquirer.id,
                company_id=self.env.user.company_id.id
            )
