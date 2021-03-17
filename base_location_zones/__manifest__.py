# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name':
    'base_location_zones',
    'version':
    '12.0.1.1.0',
    'depends': ['base_location_districts', 'base_location'],
    'author':
    "EXA Auto Parts S.A.S - Alejandro Olano Github@alejo-code",
    'license':
    "AGPL-3",
    'summary':
    '''Enhanced zip/city with zone data.''',
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/base_location_zone_view.xml',
        'views/base_location_zone_groups_view.xml',
    ],
    'installable':
    True,
    'auto_install':
    False,
}
