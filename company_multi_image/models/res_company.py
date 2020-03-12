# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    company_image_ids = fields.One2many(
        string='Company Images',
        comodel_name='res.company.image',
        inverse_name='company_id')
