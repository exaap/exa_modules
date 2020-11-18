from odoo import models, fields


class EmployeeChecklistInherit(models.Model):
    _inherit = "employee.checklist"

    department_id = fields.Many2one(comodel_name="hr.department",
                                    string="Departamento")
        
