{
    'name': 'POS Customer Type Main',
    'version': '1.0',
    'summary': 'Add a customer type selection button to the main POS screen',
    'category': 'Point of Sale',
    'author': 'Your Name',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_assets.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_customer_type_main/static/src/js/customer_type_button.js',
            'pos_customer_type_main/static/src/js/customer_type_popup.js',
            'pos_customer_type_main/static/src/css/customer_type_button.css',
        ],
    },
    'qweb': [
        'static/src/xml/customer_type_templates.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
