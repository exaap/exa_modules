# -*- coding: utf-8 -*-
# Copyright 2014 Odoo 8 - M.Hagag@DVIT.ME - http://dvit.me/
# Copyright 2018 Joan Marín <Github@JoanMarin>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Invoice Discount',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'summary': 'Show Discount Total and Total before Discount on Invoices. ',
    'author':
    'Joan Marín Github@JoanMarin, Guillermo Montoya Github@guillermm, Alejandro Olano Github@alejo-code',
    'website': 'https://github.com/exaap/exaap_modules',
    'depends': ['account'],
    'data': [
        'views/account_invoice.xml',
    ],
    'installable': True,
    'auto_install': False,
}