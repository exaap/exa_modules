# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Exa Delivery Details",
    'summary': """
			*This module adds the delivery man and its delivery datetime to sale order. 
			*This module adds delivery street in the invoice report. 
		""",
    'author': "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    'website': "https://www.exaap.com/",
    'category': 'Utility',
    'version': '10.0.0',
    'depends': ['base', 'sale', 'hr'],
    'data': [
        'views/sale_order_inherit.xml',
    ],
    'installable': True,
}
