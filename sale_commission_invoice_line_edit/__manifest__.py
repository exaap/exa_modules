# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Invoice',
    'version': '11.0.1.0.0',
    'author': 'Odoo Community Association (OCA)',
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