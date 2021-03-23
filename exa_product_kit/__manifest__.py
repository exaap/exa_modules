# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name":
    "EXA Product Kit",
    "author":
    "EXA Auto Parts Github@exaap, "
    "Joan Marín Github@JoanMarin, "
    "Alejandro Olano Github@alejo-code",
    "license":
    "AGPL-3",
    "category":
    "EXA Modules",
    "version":
    "12.0.1.0.0",
    "website":
    "https://github.com/exaap/exaap_modules",
    "installable":
    True,
    "images": [],
    "depends": ["exa_base_modules", "sale", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/account_invoice_views.xml",
        "views/product_template_views.xml",
        "views/sale_order_views.xml",
        "views/stock_move_views.xml",
    ],
}
