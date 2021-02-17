# -*- coding: utf-8 -*-
# Copyright 2019 EXA Auto Parts S.A.S Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name":
    "EXA Partner View",
    "version":
    "11.0.1.0.0",
    "license":
    "AGPL-3",
    "website":
    "https://github.com/exaap/exaap_modules",
    "author":
    "EXA Auto Parts Github@exaap, "
    "Joan Marín Github@JoanMarin, "
    "Alejandro Olano Github@alejo-code",
    "category":
    "EXA Modules",
    "depends": [
        "account", "sale_commission", "base_partner_prospect", "contacts",
        "exa_base_modules", "exa_partner_corporate_commercial", "mail", "sale",
        "purchase", "partner_company_type", "account_financial_risk",
        "product", "sale_multi_salesperson"
    ],
    "data": ["data/res_groups_data.xml", "views/res_partner_views.xml"],
    "installable":
    True,
}
