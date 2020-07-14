# -*- coding: utf-8 -*-
# Copyright 2019 EXA Auto Parts S.A.S Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "EXA Partner View",
    "version": "10.0.1.0.0",
    "license": "AGPL-3",
    "website": "https://github.com/exaap/exaap_modules",
    "author": "EXA Auto Parts Github@exaap, "
              "Joan Marín Github@JoanMarin",
    "category": "EXA Modules",
    "depends": [
        "account",
        "base_partner_prospect",
        "contacts",
        "exa_base_modules",
        "exa_partner_corporate_commercial",
        "mail",
        "partner_company_type",
        "partner_financial_risk",
        "partner_sector",
        "product",
        "sale_commission",
    ],
    "data": [
        "data/res_groups_data.xml",
        "views/res_partner_views.xml"
    ],
    "installable": True,
}
