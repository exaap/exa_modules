# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@joanodoo>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields
from collections import defaultdict


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    def _create_account_move_line(self, move, credit_account_id,
                                  debit_account_id, journal_id):
        # group quants by cost
        quant_cost_qty = defaultdict(lambda: 0.0)

        for quant in self:
            quant_cost_qty[quant.cost] += quant.qty

        AccountMove = self.env['account.move']

        for cost, qty in quant_cost_qty.iteritems():
            # Ajuste de asientos contables para produccion
            if move.production_id:
                move = move.with_context(
                    force_valuation_amount=move.price_unit)

            move_lines = move._prepare_account_move_line(
                qty, cost, credit_account_id, debit_account_id)

            if move_lines:
                date = self._context.get('force_period_date',
                                         fields.Date.context_today(self))
                # Ajuste del campo ref para que tenga algun valor en una produccion.
                ref = move.picking_id and move.picking_id.name or '%s - %s' % (
                    move.name, move.product_id.code)
                #raise Warning(move.picking_id,ref)
                new_account_move = AccountMove.create({
                    'journal_id': journal_id,
                    'line_ids': move_lines,
                    'date': date,
                    'ref': ref
                })
                new_account_move.post()
                new_account_move.write({'ref': ref})