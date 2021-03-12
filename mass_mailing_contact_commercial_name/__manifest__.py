# -*- coding: utf-8 -*-
# Copyright 2020 Juan Sebastián Ocampo Ospina <juano@exaap.com>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name':
    " Mass Mailing Contact Commercial Name",
    'summary':
    """
            This module adds a commercial name to the mass mailing contact model
                """,
    'description':
    """
        This module adds a commercial name to the mass mailing contact model
    """,
    'author':
    "EXA Auto Parts S.A.S, "
    "Juan Sebastián Ocampo Ospina <juano@exaap.com>, "
    "Alejandro Olano Github@alejo-code",
    'website':
    "https://github.com/exaap/exaap_modules",
    'category':
    'Uncategorized',
    'version':
    '0.1',
    'depends': ['mass_mailing_partner', 'partner_commercial_name'],
    'data': [
        'views/mail_mass_mailing_contact_view.xml',
    ],
}