# -*- coding: utf-8 -*-
{
    'name': "hr_payroll_report",

    'summary': """
        Various payroll reports
    """,

    'description': """
        Payroll reports
    """,

    'author': "jburckel",
    'website': "https://www.mihiariipearls.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': [
        'hr_payroll',
        'date_range',
        'report_xlsx',
        'report',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/report_payslip_monthly.xml',
        'reports/report_cst_4010_a_monthly.xml',
        'reports/report_cst_4010_monthly.xml',
        'reports/action_hr_payroll_report.xml',
    ],
    'images': [
        'static/src/img/dicp.jpg',
        'static/src/img/4010a_footer.jpg',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
