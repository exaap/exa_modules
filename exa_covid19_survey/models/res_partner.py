# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        recs = self.browse()
        if name:
            recs = self.search([('display_name', operator, name)] + args,
                               limit=limit)
        if not recs:
            recs = self.search([('identification_document', operator, name)] +
                               args,
                               limit=limit)
        if not recs:
            recs = self.search([('commercial_name', operator, name)] + args,
                               limit=limit)
        if not recs:
            recs = self.search([('email', operator, name)] + args, limit=limit)
        return recs.name_get()