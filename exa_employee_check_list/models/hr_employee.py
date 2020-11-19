from odoo import models, fields


class EmployeeMasterInherit(models.Model):
    _inherit = 'hr.employee'

    entry_checklist = fields.Many2many(
        'employee.checklist',
        'entry_obj',
        'check_hr_rel',
        'hr_check_rel',
        string='Entry Process',
    )
    exit_checklist = fields.Many2many('employee.checklist',
                                      'exit_obj',
                                      'exit_hr_rel',
                                      'hr_exit_rel',
                                      string='Exit Process')
