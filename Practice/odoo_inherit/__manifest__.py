{
    'name': 'odoo_inherit',
    'version': '1.0',
    'category': 'Extra',
    'sequence': 5,
    'summary': 'odoo training',
    'depends': ['odoo_training'],

    'description': """
            module for inherit
            """,
            

    'data' : [
       'views/inherited_view.xml',
       'security/ir.model.access.csv',
    ],

    'application' : True

}
