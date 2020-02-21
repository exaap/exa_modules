# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api, _
from openerp.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_manufacturer = fields.Boolean(
        string='Is a Manufacturer',
        default=False)

    @api.multi
    def unlink(self):
        for partner in self:
            if partner.is_manufacturer:
                raise ValidationError(_("You cannot delete partners that are manufacturers."))

        return super(ResPartner, self).unlink()
