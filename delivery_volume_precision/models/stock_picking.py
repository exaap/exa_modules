# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
from odoo.addons import decimal_precision as dp


class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(digits=dp.get_precision('Stock Volume'))
