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
        'views/record.xml',
    ],

    'application' : True

}