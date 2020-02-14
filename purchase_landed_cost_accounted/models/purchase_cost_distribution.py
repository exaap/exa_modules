# -*- coding: utf-8 -*-
# Copyright 2013 Joaquín Gutierrez
# Copyright 2014-2017 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2019 Joan Marín <Github@JoanMarin>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from odoo import fields, models, api, _


class PurchaseCostDistribution(models.Model):
    _inherit = "purchase.cost.distribution"

    state = fields.Selection(selection_add=[("accounted", _("Accounted"))])

    @api.multi
    def action_open_account_move_line(self):
        line_obj = self.env["account.move.line"]
        stock_move_ids = set([x.move_id.id for x in self.cost_lines])
        lines = line_obj.search([("stock_move_id", "in", list(stock_move_ids))])

        if lines:
            mod_obj = self.env["ir.model.data"]
            model, action_id = tuple(
                mod_obj.get_object_reference(
                    "account",
                    "action_account_moves_all_a"))
            action = self.env[model].browse(action_id).read()[0]
            ids = set([x.id for x in lines])
            action["domain"] = "[('id', 'in', %s)]" % list(ids)

            return action

    @api.multi
    def get_expense_lines(self):
        line_obj = self.env["account.move.line"]

        if self.cost_lines:
            for cost_line in self.cost_lines:
                lines = line_obj.search([("stock_move_id", "=", cost_line.move_id.id)])

                for line in lines.with_context(check_move_validity=False):
                    if line.move_id.state == "posted":
                        line.move_id.button_cancel()

                    data_line = {}
                    value_without_landed_costs = cost_line.product_price_unit * line.quantity

                    if line.credit > 0.00:
                        value_without_landed_costs *= (-1)

                    data_line["value_without_landed_costs"] = value_without_landed_costs
                    line.expense_lines = [
                        (4, expense_line.id) for expense_line in cost_line.expense_lines]
                    line.write(data_line)

                for line in lines:
                    if line.move_id.state == "draft":
                        line.move_id.post()

        self.write({"state": "accounted"})

        return True

    @api.multi
    def get_value_with_landed_costs(self):
        line_obj = self.env["account.move.line"]

        if self.cost_lines:
            for cost_line in self.cost_lines:
                lines = line_obj.search([("stock_move_id", "=", cost_line.move_id.id)])

                for line in lines.with_context(check_move_validity=False):
                    if line.move_id.state == "posted":
                        line.move_id.button_cancel()

                    data_line = {
                        "debit": 0.00,
                        "credit": 0.00,
                        "balance": 0.00,
                        "debit_cash_basis": 0.00,
                        "credit_cash_basis": 0.00,
                        "balance_cash_basis": 0.00}
                    landed_costs = (line.cost_ratio * line.quantity)

                    if line.value_without_landed_costs > 0.00:
                        debit = line.value_without_landed_costs + landed_costs
                        data_line["debit"] = debit
                        data_line["debit_cash_basis"] = debit
                        data_line["balance"] = debit
                        data_line["balance_cash_basis"] = debit
                    elif line.value_without_landed_costs < 0.00:
                        credit = (line.value_without_landed_costs * (-1)) + landed_costs
                        data_line["credit"] = credit
                        data_line["credit_cash_basis"] = credit
                        data_line["balance"] = credit * (-1)
                        data_line["balance_cash_basis"] = credit * (-1)

                    line.write(data_line)

                for line in lines:
                    if line.move_id.state == "draft":
                        line.move_id.post()

        return True

    @api.multi
    def action_overwrite_move_lines(self):
        self.get_expense_lines()
        self.get_value_with_landed_costs()

        return True

    @api.multi
    def action_done(self):
        self.action_calculate()

        return super(PurchaseCostDistribution, self).action_done()

    @api.multi
    def action_cancel(self):
        super(PurchaseCostDistribution, self).action_cancel()

        self.account_move_line_sum_cost_ratio()

        return True
