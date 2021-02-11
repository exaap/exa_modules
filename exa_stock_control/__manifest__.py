# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name':
    'Exa Stock Control',
    "license":
    "AGPL-3",
    "author":
    "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    "category":
    "EXA Modules",
    "version":
    "10.0.1.0.0",
    "website":
    "https://github.com/exaap/exaap_modules",
    'depends': ['stock', 'product_brand'],
    'data': [
        'security/groups.xml', 'views/stock_inventory_views.xml',
        'views/product_product_views.xml', 'views/product_template_views.xml'
    ]
}