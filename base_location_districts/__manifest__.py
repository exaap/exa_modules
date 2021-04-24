# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name':
    'Base Location Districts',
    'version':
    '10.0.1.1.0',
    'depends': ['base', 'base_location'],
    'author':
    "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    'license':
    "AGPL-3",
    'summary':
    '''Enhanced zip/city with district data.''',
    'data': [
        'views/view_partner_inherit.xml',
        'views/res_better_zip_district_view.xml'
    ],
    'installable':
    True,
    'auto_install':
    False,
}
