# -*- coding: utf-8 -*-
# Copyright 2014 Odoo 8 - M.Hagag@DVIT.ME - http://dvit.me/ 
# Copyright 2018 Joan Marín <Github@joanodoo> 
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).#

{
    'name': 'Sale Discount',
    'version': '10.0.1.0.0',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'summary': 'Show discount total and total before discount on sales orders.',
    'author': 'Joan Marín Github@joanodoo, Guillermo Montoya Github@guillermm',
    'website': 'http://www.exaap.com',
    'depends': ['sale'],
    'data': [
        'views/sale_order.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}