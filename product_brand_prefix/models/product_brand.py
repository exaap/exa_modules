# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import re
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductBrand(models.Model):
    _inherit = "product.brand"

    prefix = fields.Char(string="Prefix", size=3)

    @api.constrains('prefix')
    def _check_prefix(self):
        for record in self:
            prefix = "[A-Z]"
            if re.match(prefix, record.prefix):
                return True
            else:
                raise UserError(
                    _("Numbers and lowercase letters are not allowed: %s" %
                      record.prefix))
