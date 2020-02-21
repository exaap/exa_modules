# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProductManufacturer(models.Model):
    _name = "product.manufacturer"
    _description = "Homolog Products with his Manufacturer"

    product_template_id = fields.Many2one(
        string='Product',
        comodel_name='product.template',
        required=True,
        ondelete='cascade')
    manufacturer_id = fields.Many2one(
        string='Manufacturer of the Homolog',
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
        domain=[('is_manufacturer', '=', True)])
    manufacturer_pref = fields.Char(
        string='Manufacturer Ref of the Homolog',
        required=True)

    def name_get(self):
        res = []

        for record in self:
            if record.manufacturer_id:
                name = u'[%s] %s' % (
                    record.manufacturer_id.name or '',
                    record.manufacturer_pref or '')
            else:
                name = u'%s' % (record.manufacturer_pref or '')

            res.append((record.id, name))

        return res

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if not args:
            args = []

        if name:
            state = self.search([
                '|',
                ('manufacturer_pref', operator, name),
                ('manufacturer_id', operator, name)] + args, limit=limit)
        else:
            state = self.search([], limit=limit)

        return state.name_get()
