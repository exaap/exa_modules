# -*- coding: utf-8 -*-

from odoo import models, fields, api

class res_partner_function(models.Model):
    _name = 'res.partner.function'

    name = fields.Char(string='Puesto de Trabajo', required=True)
    active = fields.Boolean(string="Activo", default=True)

    _sql_constraints = [
        ('res_partner_function_uniq', 'unique(name)', 'El nombre del puesto de trabajo debe ser único!')
    ]