# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name':
    "Warehouse Restrictions",
    'summary':
    """
         Warehouse and Stock Location Restriction on Users.""",
    'description':
    """
        This Module Restricts the User from Accessing Warehouse and Process Stock Moves other than allowed to Warehouses and Stock Locations.
    """,
    'author':
    "Techspawn Solutions, "
    "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    'website':
    "https://github.com/exaap/exaap_modules",
    'category':
    'Warehouse',
    'version':
    '0.2',
    'depends': ['base', 'stock'],
    'data': [
        'views/users_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
}
