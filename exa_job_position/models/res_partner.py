# -*- coding: utf-8 -*-

from odoo import models, fields, api

class exa_job_position(models.Model):
    _inherit = 'res.partner'

    function = fields.Many2one(
        'res.partner.function',
        string='Puesto de Trabajo',
        help="Used to select the partner's job position.")