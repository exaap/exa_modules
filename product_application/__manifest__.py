# -*- coding: utf-8 -*-
# Copyright 2020 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product Application",
    "license": "AGPL-3",
    "author": "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    "category": "EXA Modules",
    "version": "10.0.1.0.0",
    "website": "https://github.com/exaap/exaap_modules",
    "depends": ['sale', 'product_brand', 'exa_base_modules'],
    "data": [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/product_application.xml',
        'views/product_application_category.xml'
    ]
}
