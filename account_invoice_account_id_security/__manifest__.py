# -*- coding: utf-8 -*-
# Copyright 2021 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Choose Account in Invoice",
    "version": "10.0.1.0.0",
    "license": "AGPL-3",
    "author": "EXA Auto Parts Github@exaap, "
              "Joan Marín Github@JoanMarin",
    "website": "https://github.com/exaap/exaap_modules",
    "category": "Product",
    "depends": [
        "account",
    ],
    "summary": "Independent permission to choose account in invoice",
    "data": [
        "security/res_groups_security.xml",
        "views/account_invoice_views.xml",
    ],
    "installable": True,
}
