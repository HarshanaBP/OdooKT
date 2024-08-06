from odoo import models, fields


class WorkCenter(models.Model):
    _name = 'work.center'
    _description = 'Work Center'

    name = fields.Char(string='Name', required=True)
    hourly_cost = fields.Float(string='Hourly Cost')
