# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Multiple Sales Person for a Customer",
    "summary": "Multiple sales people for a customer (Sale Orders / Invoice).",
    "version": "11.0.1.0.0",
    "license": "AGPL-3",
    "website": "https://www.exaap.com",
    "author": "EXA Auto Parts Github@exaap, "
              "Joan Marín Github@JoanMarin",
    "category": "Sale",
    "depends": [
        "sale",
        "mail"
    ],
    "data": [
        "views/res_partner_views.xml",
        "views/sale_order_views.xml", 
        "views/account_invoice_views.xml"
    ],
    "installable": True,
}
