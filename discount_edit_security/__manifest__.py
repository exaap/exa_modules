# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name":
    "Discount Edit Security",
    "license":
    "AGPL-3",
    "author":
    "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    'category':
    'Invoicing Management',
    "version":
    "12.0.1.0.0",
    "website":
    "https://github.com/exaap/exaap_modules",
    "depends": ['account', 'sale_management'],
    "data": [
        'security/groups.xml', 'views/account_invoice_line_view.xml',
        'views/sale_order_line_view.xml'
    ]
}
