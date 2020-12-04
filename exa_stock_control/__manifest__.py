# -*- coding: utf-8 -*-
{
    'name':
    ' Exa Stock Control',
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
        'security/groups.xml', 'security/ir.model.access.csv',
        'views/stock_inventory_views.xml', 'views/product_product_views.xml',
        'views/product_template_views.xml'
    ]
}