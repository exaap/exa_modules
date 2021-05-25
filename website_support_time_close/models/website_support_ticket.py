# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class WebsiteSupportTiket(models.Model):
    _inherit = "website.support.ticket"
    time_to_close_days = fields.Integer(string="Time to close Days")
    time_to_close_hors = fields.Integer(string="Time to close Hors")
