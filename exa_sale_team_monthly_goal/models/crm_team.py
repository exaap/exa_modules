# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class SaleTeamMonthlyGoal(models.Model):
    _inherit = 'crm.team'

    monthly_goal = fields.Integer(string='Monthly target')
    lubrication = fields.Integer(string='Objective Lubrication')
    filtration = fields.Integer(string='Filtration objective')
    other_one = fields.Integer(string='Objective One')
    other_two = fields.Integer(string='Objective Two')
    other_three = fields.Integer(string='Objective Three')
