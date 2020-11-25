from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.depends('exit_checklist')
    def exit_progress(self):
        for each in self:
            total_len = self.env['employee.checklist'].search_count([
                '&',
                ('document_type', '=', 'exit'),
                ('department_id', '=', each.department_id.id)])
            exit_len = 0

            if each.exit_checklist:
                exit_checklist = self.env['employee.checklist'].search([
                '&',
                ('id', 'in', each.exit_checklist.ids),
                ('department_id', '=', each.department_id.id)])
                exit_len = len(exit_checklist)

            if total_len != 0:
                each.exit_progress = (exit_len * 100) / total_len

    @api.depends('entry_checklist')
    def entry_progress(self):
        for each in self:
            total_len = self.env['employee.checklist'].search_count([
                '&',
                ('document_type', '=', 'entry'),
                ('department_id', '=', each.department_id.id)])
            entry_len = 0

            if each.entry_checklist:
                entry_checklist = self.env['employee.checklist'].search([
                '&',
                ('id', 'in', each.entry_checklist.ids),
                ('department_id', '=', each.department_id.id)])
                entry_len = len(entry_checklist)

            if total_len != 0:
                each.entry_progress = (entry_len * 100) / total_len

    entry_progress = fields.Float(compute=entry_progress, string='Entry Progress', store=True, default=0.0)
    exit_progress = fields.Float(compute=exit_progress, string='Exit Progress', store=True, default=0.0)
