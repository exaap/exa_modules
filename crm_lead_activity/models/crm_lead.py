# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    activities_count = fields.Integer("Activities",
                                      compute='_compute_activities_count')

    @api.multi
    def _compute_activities_count(self):
        activity_data = self.env['crm.activity.report'].read_group(
            [('lead_id', 'in', self.ids)], ['lead_id'], ['lead_id'])
        mapped_data = {
            act['lead_id'][0]: act['lead_id_count']
            for act in activity_data
        }
        for lead in self:
            lead.activities_count = mapped_data.get(lead.id, 0)