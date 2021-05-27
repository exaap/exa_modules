# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Sale Team Monthly Goal",

    'summary': """
        This module add a monthly goal for the sale_team           
    """,

    'description': """
        This module add a monthly goal for the sale_team
    """,

    'author': "EXA Auto Parts S.A.S & Solutions",
    'website': "https://www.exaap.com",

    'category': 'Addon',
    'version': '11.0.0.2',

    'depends': ['crm'],

    'data': [
        #'security/ir.model.access.csv',
        'views/crm_team_form_view.xml',
    ],
}
