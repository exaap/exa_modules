# -*- coding: utf-8 -*-
{
    'name': "Equipaments - Technical Info",

    'summary': """
       This module adds technical information about the equipament""",

    'description': """
        This module adds technical information about the equipament
    """,

    'author': "EXA Auto Parts & Solutions S.A.S",
    'website': "https://www.exaap.com",

    'category': 'Human Resources',
    'version': '10.0.1.0',

    'depends': ['maintenance'],

    'data': [
        'security/res_groups_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}