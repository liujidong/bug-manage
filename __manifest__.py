# -*- coding: utf-8 -*-
{
    'name': "bug管理",

    'summary': """
        用户软件开发中bug管理""",

    'description': """
        用户软件开发中bug管理
    """,

    'author': "liujidong",
    'website': "http://www.liujidong.me",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
