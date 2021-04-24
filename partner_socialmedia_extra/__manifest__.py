# -*- coding: utf-8 -*-
# Copyright 2018 Humanitarian Logistics Organisation e.V. - Stefan Becker
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Partner Socialmedia Extra',
    'summary': 'Add social media fields to contacts',
    'version': '10.0.1.0.0',
    'author': "Joan Marín Github@joanodoo",
    'website': "https://www.exaap.com",
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
