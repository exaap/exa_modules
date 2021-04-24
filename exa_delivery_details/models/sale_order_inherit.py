# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from odoo import models, fields, api


class DeliveryDetails(models.Model):
    _inherit = 'sale.order'

    employee_id = fields.Many2one('hr.employee', string='Delivery man')
    delivery_time = fields.Datetime(string='Delivery Date')
    delivery_time_copy = fields.Datetime(string='Delivery Date Copy')

    @api.onchange('employee_id')
    def _onchange_employee(self):
        if self.employee_id:
            self.delivery_time = self.delivery_time_copy = datetime.now()
        else:
            self.delivery_time = self.delivery_time_copy = ''

    @api.model
    def create(self, vals):
        if 'delivery_time_copy' in vals:
            vals.update({'delivery_time': vals.get('delivery_time_copy')})
        return super(DeliveryDetails, self).create(vals)

    @api.multi
    def write(self, vals):
        if 'delivery_time_copy' in vals:
            vals.update({'delivery_time': vals.get('delivery_time_copy')})
        return super(DeliveryDetails, self).write(vals)
