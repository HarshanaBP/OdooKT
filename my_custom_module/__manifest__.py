{
    'name': 'My Custom Module',
    'version': '1.0',
    'summary': 'A custom module for Odoo 17',
    'description': 'Detailed description of my custom module.',
    'category': 'Custom',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'views/my_model_views.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
