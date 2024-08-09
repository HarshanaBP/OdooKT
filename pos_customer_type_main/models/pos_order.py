from odoo import models, fields

class PosOrder(models.Model):
    _inherit = 'pos.order'

    customer_type = fields.Selection(
        [('local', 'Local'), ('europe', 'Europe'), ('asian', 'Asian'), ('other', 'Other')],
        string="Customer Type"
    )
