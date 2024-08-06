from odoo import models, fields, api
from datetime import datetime


class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Custom Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    birth_year = fields.Integer(string='Birth Year', help='Enter the year of birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True,
                         help='Calculated age based on the birth year')

    @api.depends('birth_year')
    def _compute_age(self):
        for record in self:
            if record.birth_year:
                current_year = datetime.now().year
                record.age = current_year - record.birth_year
            else:
                record.age = 0

