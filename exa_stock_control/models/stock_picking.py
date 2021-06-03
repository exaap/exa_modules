# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class Picking(models.Model):
    _inherit = "stock.picking"

    min_date = fields.Datetime(
        'Scheduled Date',
        compute='_compute_scheduled_date',
        inverse='_set_scheduled_date',
        store=True,
        index=True,
        track_visibility='onchange',
        help=
        "Scheduled time for the first part of the shipment to be processed. Setting manually a value here would set it as expected date for all the stock moves."
    )

    @api.one
    @api.depends('move_lines.date_expected')
    def _compute_scheduled_date(self):
        if self.move_type == 'direct':
            self.scheduled_date = min(
                self.move_lines.mapped('date_expected')
                or [fields.Datetime.now()])
        else:
            self.scheduled_date = max(
                self.move_lines.mapped('date_expected')
                or [fields.Datetime.now()])

    @api.one
    def _set_scheduled_date(self):
        self.move_lines.write({'date_expected': self.scheduled_date})