from odoo import models, fields, api


class HrDepartmentInherit(models.Model):
    _inherit = "hr.department"

    employee_checklist_id = fields.Many2many(comodel_name="employee.checklist",
                                             inverse_name="department_id",
                                             string="Check List")
