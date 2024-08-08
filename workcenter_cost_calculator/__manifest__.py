{
    'name': 'Work Center Cost Calculator',
    'version': '1.0',
    'summary': 'Module to calculate costs in work centers',
    'description': 'Detailed description of the work center cost calculator module.',
    'category': 'Operations',
    'author': 'Malinda Gamage',
    'website': 'https://calculatecost.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/cost_sheet_views.xml',
        'views/work_center_views.xml',
        'views/cost_sheet_line_views.xml',
        'report/paperformat_cost_sheet.xml',
        'report/cost_sheet_report_template.xml',
        'report/cost_sheet_report.xml',
        'views/assets.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/workcenter_cost_calculator/static/src/css/custom_style.css',
        ],
    },
    'demo': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'external_dependencies': {
        'python': ['json'],
    },
    # 'controllers': [
    #     'workcenter_cost_calculator.controllers.cost_sheet_controller',
    #     'workcenter_cost_calculator.controllers.pos_controller',
    # ],
}
