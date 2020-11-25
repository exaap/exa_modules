from odoo import models, fields, api


class EmployeeMasterInherit(models.Model):
    _inherit = 'hr.employee'

    entry_checklist = fields.Many2many(domain=[
        '&', ('document_type', '=',
              'entry'), ('department_id', '=', 'department_id')
    ])
    exit_checklist = fields.Many2many(domain=[
        '&', ('document_type', '=',
              'exit'), ('department_id', '=', 'department_id')
    ])

    @api.depends('exit_checklist')
    def exit_progress_in(self):
        for each in self:
            total_len = self.env['employee.checklist'].search_count([
                '&', ('document_type', '=', 'exit'),
                ('department_id', '=', self.department_id.id)
            ])
            entry_len = len(each.exit_checklist)
            if total_len != 0:
                each.exit_progress = (entry_len * 100) / total_len

    @api.depends('entry_checklist')
    def entry_progress_in(self):
        for each in self:
            total_len = self.env['employee.checklist'].search_count([
                '&', ('document_type', '=', 'entry'),
                ('department_id', '=', self.department_id.id)
            ])
            entry_len = len(each.entry_checklist)
            if total_len != 0:
                each.entry_progress = (entry_len * 100) / total_len

    entry_progress = fields.Float(compute=entry_progress_in,
                                  string='Entry Progress',
                                  store=True,
                                  default=0.0)
    exit_progress = fields.Float(compute=exit_progress_in,
                                 string='Exit Progress',
                                 store=True,
                                 default=0.0)
