# -*- coding: utf-8 -*-
# Copyright 2019 Juan Sebastian Ocampo Ospina <Github@Capriatto>
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProductBarcode(models.Model):
    _name = 'product.barcode'
    _description = "Multiple Barcodes"

    name = fields.Char(string='Barcode', required=True)
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        ondelete='cascade')

    @api.constrains('name')
    def _check_name(self):
        msg1 = _("The barcode: '%s' is already assigned.\nYou will not "
                 "be able to save this product if you do not remove the duplicated barcode.")
        msg2 = _("The barcode: '%s' is already assigned to the product '%s'.\nYou will "
                 "not be able to save this product if you do not remove the duplicated barcode.")

        if self.name:
            for template in self.env['product.template'].search([]):
                if self.name == template.barcode:
                    raise ValidationError(msg1 % self.name)

            seen = set()

            for rec in self.search([]):
                for record in rec:
                    if self.browse(record.id).name in seen:
                        raise ValidationError(msg2 % (self.name, self.get_product_name()))
                    else:
                        seen.add(self.browse(record.id).name)

    def get_product_name(self):
        prod = self.search([('name', '=', self.name)])

        return str(self.browse(prod[0].id).product_id.name)

    def name_get(self):
        res = []

        for record in self:
            name = u'%s' % (record.name or '')
            res.append((record.id, name))

        return res

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if not args:
            args = []

        if name:
            state = self.search([('name', operator, name)] + args, limit=limit)
        else:
            state = self.search([], limit=limit)

        return state.name_get()
