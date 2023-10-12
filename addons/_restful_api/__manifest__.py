{
    'name': 'Custom API Module',
    'version': '1.0',
    'author': 'Your Name',
    'summary': 'Custom API Module for Odoo',
    'description': 'This module provides a RESTful API for integration with Odoo.',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'views/api_token_view.xml',

        'views/actions/api_token.xml',

        'views/menu.xml',
    ],
    'installable': True,
}