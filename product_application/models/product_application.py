# -*- coding: utf-8 -*-
# Copyright 2020 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class ProductApplications(models.Model):
    _name = "product.application"
    name = fields.Char(string="Product Application")
