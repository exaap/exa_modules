# -*- coding: utf-8 -*-
# Copyright 2020 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_apllication_id = fields.Many2one(
        comodel_name="product.application", string="Application")
    application_category_id = fields.Many2one(
        comodel_name="product.application.category",
        string="Category",
        domain=[('parent_id', '=', False)])
    application_sub_category_id = fields.Many2one(
        comodel_name="product.application.category", string="Sub Categories")
    application_segment_id = fields.Many2one(
        comodel_name="product.application.category", string="Segment")

    edit_applications_fields = fields.Boolean(
        string="Edit 'Application Fields' Field",
        compute='_get_edit_applications_field',
        store=False)

    @api.multi
    def _get_edit_applications_field(self):
        user = self.env['res.users'].search([('id', '=', self.env.user.id)])
        edit_applications_fields = False

        if user.has_group(
                'product_application.product_application_group_manager'):
            edit_applications_fields = True

        for product in self:
            product.edit_applications_fields = edit_applications_fields

    @api.onchange('application_category_id')
    def _onchange_application_category_id(self):
        self.application_sub_category_id = False
        self.application_segment_id = False

    @api.onchange('application_sub_category_id')
    def _onchange_application_sub_category_id(self):
        self.application_segment_id = False

    @api.multi
    def toggle_active(self):
        user = self.env['res.users'].search([('id', '=', self.env.user.id)])
        if not user.has_group('product_application.group_archive'):
            raise UserError(_('You cannot archive products'))
        return super(ProductTemplate, self).toggle_active()

    @api.multi
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if vals.get('product_apllication_id') or vals.get(
                'application_category_id') or vals.get(
                    'application_sub_category_id') or vals.get(
                        'application_segment_id') in vals:
            user = self.env['res.users'].search([('id', '=', self.env.user.id)
                                                 ])
            if not user.has_group('product_application.group_category'):
                raise UserError(
                    _('You can not modify applications or product categories'))
        return res
