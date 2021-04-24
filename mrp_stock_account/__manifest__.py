# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@joanodoo> 
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).#

{
    'name': 'MRP Stock',
    'category': 'Manufacturing',
    'version': '10.0.0.0.1',
    'author': 'Joan Marín Github@joanodoo, Guillermo Montoya Github@guillermm',
    'website': 'http://www.exaap.com',
    'license': 'AGPL-3',
    'summary': 'Functionalities for MRP - Odoo version 10',
    'depends': [
        'mrp',
        'stock_account'
    ],
    'data': [
        'views/mrp_production.xml',
    ],
    'installable': True,
}