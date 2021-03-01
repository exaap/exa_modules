# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class AccountServiceOrder(models.Model):
    _name = 'account.service.order'

    name = fields.Char(string='Number')
    number_x = fields.Integer(string='Number X')
    number_y_set = fields.Boolean(string='Number Y Set?', default=False)
    has_number_y = fields.Boolean(string='It Has Number Y?', default=False)
    number_y = fields.Integer(string='Number Y')
    last_created = fields.Boolean(string='Last Created?', default=False)
    description = fields.Text(string='Description')
    partner_id = fields.Many2one('res.partner',
                                 string='Customer',
                                 domain=[('customer', '=', True)])
    user_ids = fields.Many2many(comodel_name='res.users',
                                relation='account_service_order_res_users_rel',
                                column1='user_id',
                                column2='service_order_id',
                                string='Managers/Delegates')
    state = fields.Selection(selection=[('open', 'Open'),
                                        ('finished', 'Finished'),
                                        ('cancel', 'Cancel')],
                             string='State',
                             readonly=True,
                             default='open')
    move_lines = fields.One2many(comodel_name='account.move.line',
                                 inverse_name='service_order_id',
                                 string='Journal Items')
    invoice_lines = fields.One2many(comodel_name='account.invoice.line',
                                    inverse_name='service_order_id',
                                    string='Invoice Lines')

    @api.multi
    def change_state_to_open(self):
        self.state = 'open'

        return True

    @api.multi
    def change_state_to_finished(self):
        self.state = 'finished'

        return True

    @api.multi
    def change_state_to_cancel(self):
        self.state = 'cancel'
        self.remove_service_order()

        return True

    @api.multi
    def remove_service_order(self):
        for move_line in self.move_lines:
            move_line.has_service_order = 'no'
            move_line.service_order_id = False

        for invoice_line in self.invoice_lines:
            if invoice_line.invoice_id.has_service_order == 'yes':
                invoice_line.invoice_id.has_service_order = 'no'

            if invoice_line.invoice_id.has_more_service_orders:
                invoice_line.invoice_id.has_more_service_orders = False

            invoice_line.service_order_id = False

        return True

    @api.multi
    def set_name(self):
        for service_order in self:
            if not service_order.number_x and not service_order.number_x:
                service_orders = self.env['account.service.order'].search([])
                service_orders_last_created = self.env[
                    'account.service.order'].search([('last_created', '=',
                                                      True)])
                number_x_before = max(service_orders.mapped('number_x')) or 0
                number_x = number_x_before + 1
                number_y = 1

                for service_order_last_created in service_orders_last_created:
                    service_order_last_created.last_created = False

                if not service_order.has_number_y:
                    service_order.write({
                        'name': str(number_x),
                        'number_x': number_x,
                        'number_y': number_y,
                        'last_created': True
                    })
                else:
                    service_orders_number_y = self.env[
                        'account.service.order'].search([('number_x', '=',
                                                          number_x_before)])

                    if service_orders_number_y:
                        number_y = max(
                            service_orders_number_y.mapped('number_y'))
                        number_y = number_y + 1

                    if number_x_before != 0:
                        number_x = number_x_before

                    service_order.write({
                        'name':
                        str(number_x) + '.' + str(number_y),
                        'number_x':
                        number_x,
                        'number_y':
                        number_y,
                        'number_y_set':
                        True,
                        'last_created':
                        True
                    })

        return True

    @api.model
    def create(self, vals):
        res = super(AccountServiceOrder, self).create(vals)
        res.set_name()

        return res

    @api.multi
    def write(self, vals):
        rec = super(AccountServiceOrder, self).write(vals)

        if vals.get('name'):
            for service_order in self:
                if service_order.number_x and service_order.number_y:
                    name = str(service_order.number_x) + '.' + str(
                        service_order.number_y)

                    if (vals.get('name') == name or vals.get('name') == str(
                            service_order.number_x)):
                        return rec
                    else:
                        raise UserError(
                            _('You do not have permission to edit this, ' +
                              'contact your administrator if you have any problems.'
                              ))
        else:
            return rec

    @api.multi
    def unlink(self):
        service_orders_obj = self.env['account.service.order']

        for service_order in self:
            if not service_order.last_created:
                raise UserError(
                    _('You can only delete the last service order at a time, '
                      +
                      'contact your administrator if you have any problems.'))

            service_order.remove_service_order()
            res = super(AccountServiceOrder, self).unlink()
            service_orders = service_orders_obj.search([])

            if service_orders:
                max_number_x = max(service_orders.mapped('number_x')) or 0
                service_orders = service_orders_obj.search([('number_x', '=',
                                                             max_number_x)])

            if service_orders:
                max_number_y = max(service_orders.mapped('number_y'))
                max_service_order = service_orders_obj.search([
                    ('number_x', '=', max_number_x),
                    ('number_y', '=', max_number_y)
                ])
                max_service_order.last_created = True

        return res

    @api.onchange('has_number_y')
    def _onchange_has_number_y(self):
        for service_order in self:
            if service_order.name:
                if service_order.has_number_y:
                    name = str(service_order.number_x) + '.' + str(
                        service_order.number_y)
                    service_order.name = name
                    service_order.number_y_set = True
