from odoo import models, fields, api


class CostSheetLine(models.Model):
    _name = 'cost.sheet.line'
    _description = 'Cost Sheet Line'

    cost_sheet_id = fields.Many2one('cost.sheet', string='Cost Sheet')
    work_center_id = fields.Many2one('work.center', string='Work Center')
    hours_spent = fields.Float(string='Hours Spent')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('hours_spent', 'work_center_id.hourly_cost')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.hours_spent * line.work_center_id.hourly_cost
