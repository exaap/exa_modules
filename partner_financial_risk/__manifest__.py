# -*- coding: utf-8 -*-
# Copyright 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name':
    'Partner Financial Risk',
    'summary':
    'Manage partner risk',
    'version':
    '11.0.1.0.1',
    'category':
    'Sales Management',
    'license':
    'AGPL-3',
    'author':
    'Tecnativa, Odoo Community Association (OCA), '
    'EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code',
    'website':
    'https://github.com/exaap/exaap_modules',
    'depends': [
        'account',
    ],
    'data': [
        'data/partner_financial_risk_data.xml',
        'views/res_config_view.xml',
        'views/res_partner_view.xml',
        'wizard/partner_risk_exceeded_view.xml',
        'templates/assets.xml',
    ],
    'installable':
    True,
}
