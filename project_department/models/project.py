# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    project_department_id = fields.Many2one(related='project_id.department_id',
                                            string='Project Department',
                                            store=True)


class Project(models.Model):
    _inherit = "project.project"

    department_id = fields.Many2one(
        related='analytic_account_id.department_id',
        string='Project Department',
        readonly=False)
