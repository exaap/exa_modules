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

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        res = super(ProductProduct, self).name_search(name, args, operator, limit)
        args = args or []
        recs = []
        domain = [('barcode_ids', operator, name)]

        if name:
            recs = self.search(domain + args, limit=limit)
        else:
            recs = self.search(args, limit=limit)

        return res + recs.name_get()

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
