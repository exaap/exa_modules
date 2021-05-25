# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HrDepartmentInherit(models.Model):
    _inherit = "hr.department"

    employee_checklist_id = fields.Many2many(comodel_name="employee.checklist",
                                             inverse_name="department_id",
                                             string="Check List")
