{
    'name': 'odoo_training',
    'version': '1.0',
    'category': 'Extra',
    'sequence': 5,
    'summary': 'odoo tarining',
    'depends': ['base'],

    'description': """
            training module
            """,

    'data' : [
        'security/ir.model.access.csv',
        'wizard/wizard_template.xml',
        'views/record.xml',
        'report/car_report.xml',
        'report/report_template.xml',
    ],

    'application' : True

}