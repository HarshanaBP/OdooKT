# workcenter_cost_calculator/controllers/cost_sheet_controller.py

from odoo import http
from odoo.http import request
import json
from datetime import date, datetime

def date_handler(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    raise TypeError("Type not serializable")

class CostSheetController(http.Controller):

    @http.route('/api/cost_sheets', type='http', auth='none', methods=['GET'], csrf=False)
    def get_all_cost_sheets(self, **kwargs):
        try:
            cost_sheets = request.env['cost.sheet'].sudo().search([])
            cost_sheets_data = []
            for sheet in cost_sheets:
                sheet_data = sheet.read(['name', 'date_field', 'total_cost'])[0]
                line_data = []
                for line in sheet.line_ids:
                    line_data.append({
                        'id': line.id,
                        'cost_sheet_id': line.cost_sheet_id.id,
                        'work_center_id': line.work_center_id.id,
                        'hours_spent': line.hours_spent,
                        'subtotal': line.subtotal,
                    })
                sheet_data['line_ids'] = line_data
                cost_sheets_data.append(sheet_data)

            return request.make_response(json.dumps(cost_sheets_data, default=date_handler), 
                                         headers=[('Content-Type', 'application/json')])
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}),
                                         headers=[('Content-Type', 'application/json')], status=500)

    @http.route('/api/cost_sheets/<int:id>', type='http', auth='none', methods=['GET'], csrf=False)
    def get_cost_sheet_by_id(self, id, **kwargs):
        try:
            cost_sheet = request.env['cost.sheet'].sudo().browse(id)
            if not cost_sheet:
                return request.make_response(json.dumps({'error': 'Cost sheet not found'}),
                                             headers=[('Content-Type', 'application/json')], status=404)
            cost_sheet_data = cost_sheet.read(['name', 'date_field', 'total_cost'])[0]
            line_data = []
            for line in cost_sheet.line_ids:
                line_data.append({
                    'id': line.id,
                    'cost_sheet_id': line.cost_sheet_id.id,
                    'work_center_id': line.work_center_id.id,
                    'hours_spent': line.hours_spent,
                    'subtotal': line.subtotal,
                })
            cost_sheet_data['line_ids'] = line_data
            return request.make_response(json.dumps(cost_sheet_data, default=date_handler), 
                                         headers=[('Content-Type', 'application/json')])
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}),
                                         headers=[('Content-Type', 'application/json')], status=500)
