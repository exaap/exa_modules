# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class EmployeeChecklistInherit(models.Model):
    _inherit = "employee.checklist"

    department_id = fields.Many2many(comodel_name="hr.department",
                                     string="Departamento")
