# -*- coding: utf-8 -*-
# Copyright 2019 Juan Sebastian Ocampo Ospina <Github@Capriatto>
# Copyright 2020 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Product Multiple Barcodes",
    "author": "EXA Auto Parts Github@exaap, "
              "Juan Sebastian Ocampo Ospina Github@Capriatto, "
              "Joan Marín Github@JoanMarin",
    "license": "AGPL-3",
    "category": "Product",
    "version": "10.0.1.0.0",
    "website": "https://github.com/exaap/exaap_modules",
    "installable": True,
    "images": ["static/description/main_banner.png"],
    "depends": [
        "product_multi_manufacturer"
    ],
    "data": [
        "security/res_groups_security.xml",
        "security/ir.model.access.csv",
        "views/product_product_views.xml",
        "views/product_template_views.xml",
    ],
}
