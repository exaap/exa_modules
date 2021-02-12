# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name":
    "Product Application",
    "license":
    "AGPL-3",
    "author":
    "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    'category':
    'Warehouse',
    "version":
    "12.0.1.0.0",
    "website":
    "https://github.com/exaap/exaap_modules",
    "depends": ['sale_management'],
    "data": [
        'security/groups.xml', 'security/ir.model.access.csv',
        'views/product_template.xml', 'views/product_application.xml',
        'views/product_application_category.xml', 'views/product_product.xml'
    ]
}
