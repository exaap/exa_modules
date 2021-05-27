# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class exa_job_position(models.Model):
    _inherit = 'res.partner'

    function = fields.Many2one(
        'res.partner.function',
        string='Puesto de Trabajo',
        help="Used to select the partner's job position.")