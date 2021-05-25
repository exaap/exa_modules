# -*- coding: utf-8 -*-
#  Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.multi
    @api.constrains('email')
    def _check_email(self):
        for partner in self:
            email_exceptions = self.env["res.partner.email.exception"].search(
                []).mapped("name")
            domain = [('id', '!=', partner.id), ('email', '=', partner.email),
                      ('email', '!=', False),
                      ('email', '!=', email_exceptions)]
            other_partners = self.search(domain)

            # active_test is False when called from
            # base.partner.merge.automatic.wizard
            if other_partners and self.env.context.get("active_test", True):
                raise ValidationError(
                    _("This email is already set to partner '%s'") %
                    other_partners[0].display_name)
