# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    quants_recalculated = fields.Boolean(
        string="Quants Recalculated?",
        default=False)
    last_date_quants_recalculated = fields.Datetime(
        string="Last Date of Recalculated Quants",
        default=False)
