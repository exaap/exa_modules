# -*- coding: utf-8 -*-
# Copyright 2018 Humanitarian Logistics Organisation e.V. - Stefan Becker
# Copyright 2020 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Exa Delivery Details",
    'summary':
    """ *This module adds the delivery man and its delivery datetime to sale order.I *This module adds delivery street in the invoice report.
	""",
    'version': '12.0.1.0.0',
    'author': "Joan Marín Github@JoanMarin, "
    "Alejandro Olano Github@alejo-code",
    'website': "https://github.com/exaap/exaap_modules",
    'depends': ['base', 'sale', 'hr'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
}
