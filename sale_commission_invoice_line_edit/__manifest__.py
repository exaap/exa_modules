# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Invoice',
    'version': '10.0.1.0.0',
    'author':
    'EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code, Odoo Community Association (OCA)',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'depends': [
        'sale_commission',
    ],
    'data': [
        'views/account_invoice_line_view.xml',
    ],
    'installable': True,
}