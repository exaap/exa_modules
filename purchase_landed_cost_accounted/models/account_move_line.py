# -*- coding: utf-8 -*-
# Copyright 2013 Joaquín Gutierrez
# Copyright 2014-2017 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2019 Joan Marín <Github@JoanMarin>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from odoo import fields, models, api
import openerp.addons.decimal_precision as dp


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.multi
    @api.depends("expense_lines", "expense_lines.cost_ratio")
    def _compute_cost_ratio(self):
        for move_line in self:
            cost_ratio = 0

            for expense_line in move_line.expense_lines:
                if expense_line.distribution_line.distribution.state == "accounted":
                    cost_ratio += expense_line.cost_ratio

            move_line.cost_ratio = cost_ratio

    cost_ratio = fields.Float(
        string="Unit Cost",
        digits=dp.get_precision("Account"),
        compute="_compute_cost_ratio")
    expense_lines = fields.Many2many(
        comodel_name="purchase.cost.distribution.line.expense",
        relation="account_move_line_distribution_line_expense_rel",
        column1="move_line_id",
        column2="distribution_line_expense_id",
        string="Expenses in Journal Items")
    value_without_landed_costs = fields.Float(
        string="Value Without Landed Costs",
        digits=dp.get_precision("Account"),
        default=0.00)
