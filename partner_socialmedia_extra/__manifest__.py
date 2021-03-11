# -*- coding: utf-8 -*-
# Copyright 2018 Humanitarian Logistics Organisation e.V. - Stefan Becker
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Partner Socialmedia Extra',
    'summary': 'Add social media fields to contacts',
    'version': '11.0.1.0.0',
    'author': "Joan Marín Github@JoanMarin, "
    "Alejandro Olano Github@alejo-code",
    'website': "https://github.com/exaap/exaap_modules",
    'category': 'CRM',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'partner_socialmedia',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
}
