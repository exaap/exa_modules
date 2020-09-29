# -*- coding: utf-8 -*-
{
    'name': "EXA Partner Job Position",
    'author': "EXA Auto Parts & Solutions S.A.S",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'summary': """
        Used to select the partner's job position in a drop-down list.
        """,
    'description': """
        Used to select the partner's job position in a drop-down list.
    """,
    'website': "http://www.exaap.com",
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/res_partner_function.xml',
        'views/res_partner.xml',
        'data/res_partner_job.xml'
    ],
}