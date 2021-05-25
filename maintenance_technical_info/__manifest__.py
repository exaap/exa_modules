# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Equipaments - Technical Info",

    'summary': """
       This module adds technical information about the equipament""",

    'description': """
        This module adds technical information about the equipament
    """,

    "author": "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    'website': "https://www.exaap.com",

    'category': 'Human Resources',
    'version': '11.0.1.0',

    'depends': ['maintenance'],

    'data': [
        'security/res_groups_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}