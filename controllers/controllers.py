# -*- coding: utf-8 -*-
from odoo import http

# class HrPayrollReport(http.Controller):
#     @http.route('/hr_payroll_report/hr_payroll_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_payroll_report/hr_payroll_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_payroll_report.listing', {
#             'root': '/hr_payroll_report/hr_payroll_report',
#             'objects': http.request.env['hr_payroll_report.hr_payroll_report'].search([]),
#         })

#     @http.route('/hr_payroll_report/hr_payroll_report/objects/<model("hr_payroll_report.hr_payroll_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_payroll_report.object', {
#             'object': obj
#         })