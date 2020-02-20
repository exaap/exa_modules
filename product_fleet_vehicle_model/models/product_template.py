# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    fleet_vehicle_model_ids = fields.Many2many(
        comodel_name="fleet.vehicle.model",
        string="Vehicle Model")
