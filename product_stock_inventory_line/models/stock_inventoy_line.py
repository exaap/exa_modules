# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

class StockInventoryLine(models.Model):
    _inherit = "stock.inventory.line"

    date = fields.Datetime(related="inventory_id.date")
