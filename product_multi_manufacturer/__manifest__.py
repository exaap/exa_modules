# -*- coding: utf-8 -*-
# Copyright 2018 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Homolog Products with his Manufacturer",
    "version": "11.0.1.0.0",
    "license": "AGPL-3",
    "author": "EXA Auto Parts Github@exaap, "
              "Joan Marín Github@JoanMarin",
    "website": "https://github.com/exaap/exaap_modules",
    "category": "Product",
    "depends": [
        "product_manufacturer",
    ],
    "summary": "Relate alternative references to the product",
    "data": [
        "security/ir.model.access.csv",
        "views/product_product_views.xml",
        "views/product_template_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
}
