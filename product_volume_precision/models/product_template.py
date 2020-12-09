# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
import odoo.addons.decimal_precision as dp

class ProductTemplate(models.Model):
    _inherit = "product.template"

    volume = fields.Float(digits=dp.get_precision('Stock Volume'))
