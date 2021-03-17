# -*- coding: utf-8 -*-
# Copyright 2018 Humanitarian Logistics Organisation e.V. - Stefan Becker
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Partner Socialmedia',
    'summary': 'Add social media fields to contacts',
    'version': '12.0.1.0.0',
    'author': "humanilog, Odoo Community Association (OCA), "
    "Alejandro Olano Github@alejo-code",
    'website': "https://github.com/exaap/exaap_modules",
    'category': 'CRM',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'base',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
}
