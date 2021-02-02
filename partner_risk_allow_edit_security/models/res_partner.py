# -*- coding: utf-8 -*-
# Copyright 2021 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    risk_allow_edit = fields.Boolean(compute='_compute_risk_allow_edit')

    @api.multi
    def _compute_risk_allow_edit(self):
        res = super(ResPartner, self)._compute_risk_allow_edit()
        is_editable = self.env.user.has_group(
            'partner_risk_allow_edit_security.group_partner_risk_allow_edit'
        )

        for partner in self.filtered('customer'):
            partner.risk_allow_edit = is_editable

        return res
