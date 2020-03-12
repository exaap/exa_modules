# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompanyImage(models.Model):
    _name = "res.company.image"
    _description = "Company Images"

    company_id = fields.Many2one(
        string='Company',
        comodel_name='res.company',
        required=True,
        ondelete='cascade')
    image_filename = fields.Char(string='Filename')
    image_file = fields.Binary(string='File')
