# -*- coding: utf-8 -*-
{
    'name': "Basic Salary Quick Update",

    'summary': """
       Basic Salary Quick Update""",

    'description': """
        Basic Salary Quick Update, Update Contracts Wage Quickly, Employees Update Basic salary
    """,

    'author': "Kaizen Principles",
    'website': "http://www.kaizeae.com",

    'category': 'HR',
    'version': '.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_contract'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_contract.xml',
        'wizard/salary_update_wizard.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,

}
