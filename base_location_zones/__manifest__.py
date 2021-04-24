# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name':
    'Base Location Zones',
    'version':
    '10.0.1.1.0',
    'depends': ['base_location_districts'],
    'author':
    "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    'license':
    "AGPL-3",
    'summary':
    '''Enhanced zip/city with zone data.''',
    'data': [
        'security/ir.model.access.csv',
        'views/view_partner_inherit.xml',
        'views/base_location_zone_view.xml',
        'views/base_location_zone_groups_view.xml',
    ],
    'installable':
    True,
    'auto_install':
    False,
}
