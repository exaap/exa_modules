# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

{
    'name':
    'Service Orders',
    'version':
    '12.0.1.0.0',
    'category':
    'Account',
    "author":
    "EXA Auto Parts Github@exaap, "
    "Joan Marín Github@JoanMarin, "
    "Alejandro Olano Github@alejo-code",
    'website':
    'https://github.com/exaap/exaap_modules',
    'summary':
    'Service Orders',
    'depends': [
        'account',
    ],
    'data': [
        'data/res_groups_data.xml',
        'security/ir.model.access.csv',
        'views/account_service_order_view.xml',
        'views/account_account_view.xml',
        'views/account_move_line_view.xml',
        'views/account_invoice_view.xml',
    ],
    'installable':
    True,
    'images': [],
    'license':
    'AGPL-3',
}
