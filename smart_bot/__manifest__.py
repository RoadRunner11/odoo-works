# -*- coding: utf-8 -*-
{
    'name': "smart_bot",

    'summary': """
        Extends the abiltities of the OdooBot""",

    'description': """
        The Purpose of this module is to make sure that 
        we can have a relatively intelligent bot, that's why we 
        are calling it smart bot
    """,

    'author': "AKOREDE FODILU OLAWALE",
    'website': "http://erp.ehiotech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail_bot'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
