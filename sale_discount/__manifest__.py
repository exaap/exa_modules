# -*- coding: utf-8 -*-
# Copyright 2014 Odoo 8 - M.Hagag@DVIT.ME - http://dvit.me/
# Copyright 2018 Joan Marín <Github@joanodoo>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Discount',
    'version': '11.0.1.0.0',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'summary':
    'Show discount total and total before discount on sales orders.',
    'author':
    'Joan Marín Github@joanodoo, Guillermo Montoya Github@guillermm, Alejandro Olano Github@alejo-code',
    'website': 'https://github.com/exaap/exaap_modules',
    'depends': ['sale', 'sale_management'],
    'data': [
        'views/sale_order.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}