# -*- coding: utf-8 -*-
# Copyright 2019 VentorTech OU
# Copyright 2019 Juan Sebastian Ocampo Ospina <Github@Capriatto>
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    barcode_ids = fields.One2many(
        related='product_variant_ids.barcode_ids',
        readonly=False)

    @api.constrains('barcode')
    def _constrains_barcode(self):
        msg = _("The barcode: '%s' is already assigned to the product '%s'.\nYou will "
                "not be able to save this product if you do not remove the duplicated barcode.")

        if self.barcode:
            prod = self.env['product.barcode.multi'].search([('name', '=', self.barcode)])

            if prod:
                raise ValidationError(msg % (self.barcode, self.get_product_name()))

    def get_product_name(self):
        obj = self.env['product.barcode.multi']
        prod = obj.search([('name', '=', self.barcode)])

        return obj.browse(prod[0].id).product_id.product_tmpl_id.name
