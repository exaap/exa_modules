# -*- coding: utf-8 -*-
# Copyright 2020 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class PartnerEmailException(models.Model):
    _name = "res.partner.email.exception"

    name = fields.Char(string="Email Exceptions")
