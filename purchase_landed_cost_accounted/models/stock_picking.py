# -*- coding: utf-8 -*-
# Copyright 2013 Joaquín Gutierrez
# Copyright 2014-2017 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2019 Joan Marín <Github@JoanMarin>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from odoo import models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def action_open_account_move_line(self):
        line_obj = self.env['account.move.line']
        lines = line_obj.search([('stock_move_id', 'in', self.move_lines.ids)])

        if lines:
            mod_obj = self.env['ir.model.data']
            model, action_id = tuple(
                mod_obj.get_object_reference(
                    'account',
                    'action_account_moves_all_a'))
            action = self.env[model].browse(action_id).read()[0]
            ids = set([x.id for x in lines])
            action['domain'] = "[('id', 'in', %s)]" % list(ids)

            return action
