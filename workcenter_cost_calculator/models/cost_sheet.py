from odoo import models, fields, api


class CostSheet(models.Model):
    _name = 'cost.sheet'
    _description = 'Cost Sheet'

    name = fields.Char(string='Name', required=True)
    date_field = fields.Date(string='Date', help='Date of Cost Sheet Issued',
                             default=fields.Date.today())
    total_cost = fields.Float(string='Total Cost', compute='_compute_total_cost', store=True)
    line_ids = fields.One2many('cost.sheet.line', 'cost_sheet_id', string='Cost Sheet Lines')

    @api.depends('line_ids.subtotal')
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = sum(line.subtotal for line in record.line_ids)
