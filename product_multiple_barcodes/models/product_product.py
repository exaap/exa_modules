# -*- coding: utf-8 -*-
# Copyright 2019 VentorTech OU
# Copyright 2019 Juan Sebastian Ocampo Ospina <Github@Capriatto>
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    barcode_ids = fields.One2many(
        comodel_name='product.barcode.multi',
        inverse_name='product_id',
        string='Additional Barcodes')

    @api.multi
    def write(self, vals):
        """
        The write function is overridden to prevent duplicated lines.
        """
        msg = _("Alert! The following barcodes are duplicated: %s")
        seen = set()
        string_created = ""
        res = super(ProductProduct, self).write(vals)

        for record in self.barcode_ids:
            if record.name in seen:
                string_created += "\n\n" + record.name
            else:
                seen.add(record.name)

        if string_created:
            raise ValidationError(msg % string_created)

        return res
