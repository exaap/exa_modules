# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name':
    "EXA Partner Job Position",
    'author':
    "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    'version':
    '11.0.1.0.0',
    'license':
    'AGPL-3',
    'summary':
    """
        Used to select the partner's job position in a drop-down list.
        """,
    'description':
    """
        Used to select the partner's job position in a drop-down list.
    """,
    'website':
    "http://www.exaap.com",
    'category':
    'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/res_partner_function.xml', 'views/res_partner.xml',
        'data/res_partner_job.xml'
    ],
}