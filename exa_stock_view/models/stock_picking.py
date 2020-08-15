# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    partner_street = fields.Char(related='partner_id.street')
    partner_district_id = fields.Many2one(related='partner_id.district_id')
    partner_zone_id = fields.Many2one(related='partner_id.zone_id')
    partner_zip_id = fields.Many2one(related='partner_id.zip_id')
