# -*- coding: utf-8 -*-
#  Copyright 2020 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name":
    "Partner unique email Exceptions",
    "summary":
    "Add Exaceptions an unique constraint to email field",
    "author":
    "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    "version":
    "10.0.1.0.0",
    "website":
    "https://github.com/exaap/exaap_modules",
    "license":
    "AGPL-3",
    "installable":
    True,
    "depends": [
        "partner_email_unique",
    ],
    "data": [
        "security/ir.model.access.csv", "security/groups.xml",
        "views/res_config.xml"
    ]
}
