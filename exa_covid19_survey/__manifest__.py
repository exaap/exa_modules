# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'COVID19 ENCUESTA',
    'author': 'EXA Auto Parts S.A.S & Solutions.',
    'version': '1.0',
    'category': 'Human Resources',
    'description': """
        Survey for partners of EXA Auto Parts & Solutions.""",
    'depends': ['l10n_co_partner_vat'],
    'summary': 'Covid19, Surveys',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/survey_views.xml'
            ],
    'installable': True,
    'application': True,
}
