# -*- coding: utf-8 -*-
# Part of Cruze. See LICENSE file for full copyright and licensing details.
{
    'name': 'Travel Booking',
    'version': '1.0',
    'summary': 'Manage booking durations',
    'sequence': 25,
    'description': """
Simple Travel Booking for Odoo Sales
===========================================
Description is a todo.
    """,
    'category': 'Sales/Sales',
    'author': 'Cubex Solutions',
    'website': 'https://www.cubex.solutions',
    'price': 5,
    'currency': 'USD',
    'images': [],
    'depends': ['sale_management'],
    'data': [
        'views/product.xml',
        'views/sale_order.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    # 'post_init_hook': '_auto_install_l10n',
}
