# -*- coding: utf-8 -*-
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name':
    "CRM Lead Activity",
    'version':
    "10.0.1.0.0",
    'author':
    "Joan Marín Github@JoanMarin",
    'category':
    "CRM",
    'summary':
    "View crm_activity_log",
    'license':
    'LGPL-3',
    'data': [
        'report/crm_activity_report_views.xml',
        'views/crm_lead_views.xml',
        'wizard/crm_activity_log_views.xml',
    ],
    'demo': [],
    'depends': ['crm'],
    'images': [],
    'installable':
    True,
}
