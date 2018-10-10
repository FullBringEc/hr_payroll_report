# -*- coding: utf-8 -*-
# Author: Jonathan Burckel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval


class PayslipMonthlyReportWizard(models.TransientModel):
    """Payslip monthly report wizard."""

    _name = "payslip.monthly.report.wizard"
    _description = "Payslip Monthly Report Wizard"

    company_id = fields.Many2one(
        comodel_name='res.company',
        default=lambda self: self.env.user.company_id,
        string='Company'
    )
    date_range_id = fields.Many2one(
        comodel_name='date.range',
        string='Date range'
    )
    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)
    fy_start_date = fields.Date(compute='_compute_fy_start_date')

    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        string='Filter employee',
    )

    @api.depends('date_from')
    def _compute_fy_start_date(self):
        for wiz in self.filtered('date_from'):
            date = fields.Datetime.from_string(wiz.date_from)
            res = self.company_id.compute_fiscalyear_dates(date)
            wiz.fy_start_date = res['date_from']

    @api.onchange('date_range_id')
    def onchange_date_range_id(self):
        """Handle date range change."""
        self.date_from = self.date_range_id.date_start
        self.date_to = self.date_range_id.date_end

    @api.multi
    def button_export_html(self):
        self.ensure_one()
        action = self.env.ref(
            'payroll_report_qweb.action_report_payslip_monthly')
        vals = action.read()[0]
        context1 = vals.get('context', {})
        if isinstance(context1, basestring):
            context1 = safe_eval(context1)
        model = self.env['report_payslip_monthly_qweb']
        report = model.create(self._prepare_report_payslip_monthly())
        report.compute_data_for_report()
        context1['active_id'] = report.id
        context1['active_ids'] = report.ids
        vals['context'] = context1
        return vals

    @api.multi
    def button_export_pdf(self):
        self.ensure_one()
        report_type = 'qweb-pdf'
        return self._export(report_type)

    @api.multi
    def button_export_xlsx(self):
        self.ensure_one()
        report_type = 'xlsx'
        return self._export(report_type)

    def _prepare_report_general_ledger(self):
        self.ensure_one()
        return {
            'date_from': self.date_from,
            'date_to': self.date_to,
            'company_id': self.company_id.id,
            'filter_account_ids': [(6, 0, self.account_ids.ids)],
            'filter_employee_ids': [(6, 0, self.employee_ids.ids)],
            'fy_start_date': self.fy_start_date,
        }

    def _export(self, report_type):
        """Default export is PDF."""
        model = self.env['report_payslip_monthly_qweb']
        report = model.create(self._prepare_report_payslip_monthly())
        report.compute_data_for_report()
        return report.print_report(report_type)
