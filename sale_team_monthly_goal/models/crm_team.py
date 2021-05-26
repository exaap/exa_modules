# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sale_team_monthly_goal(models.Model):
    _inherit = 'crm.team'
    
    monthly_goal = fields.Integer('Objetivo mensual')
    lubrication = fields.Integer('Objetivo Lubricación')
    filtration = fields.Integer('Objetivo Filtración')
    other_one = fields.Integer('Objetivo Uno')
    other_two = fields.Integer('Objetivo Dos')
    other_three = fields.Integer('Objetivo Tres')
