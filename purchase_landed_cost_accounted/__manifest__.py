# -*- coding: utf-8 -*-
# Copyright 2013 Joaquín Gutierrez
# Copyright 2014-2017 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2019 Joan Marín <Github@JoanMarin>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

{
    "name": "Extension to 'Purchase landed costs - Alternative option'",
    "version": "10.0.1.0.0",
    "license": "AGPL-3",
    "author": "OdooMRP team, "
              "AvanzOSC, "
              "Tecnativa, "
              "Joaquín Gutierrez, "
              "EXA Auto Parts Github@exaap, "
              "Joan Marín Github@JoanMarin, "
              "Odoo Community Association (OCA)",
    "category": "Purchase Management",
    "website": "https://github.com/exaap/exaap_modules",
    "summary": "Purchase cost distribution",
    "depends": [
        "purchase_landed_cost",
        "account_move_line_stock_info",
    ],
    "data": [
        "views/stock_picking_views.xml",
        "views/purchase_cost_distribution_views.xml",
        "views/account_move_line_views.xml",
    ],
    "installable": True,
}
