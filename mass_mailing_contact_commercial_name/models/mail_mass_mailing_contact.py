# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class mass_mailing_contact_commercial_name(models.Model):
    _inherit = 'mail.mass_mailing.contact'

    commercial_name = fields.Char(related='partner_id.commercial_name',
                                  string="Empresa",
                                  store=True)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        res = super(mass_mailing_contact_commercial_name,
                    self)._onchange_partner()
        if self.partner_id:
            self.commercial_name = self.partner_id.commercial_name
