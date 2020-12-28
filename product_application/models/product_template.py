# -*- coding: utf-8 -*-
# Copyright 2020 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


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