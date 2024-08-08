from odoo import http
from odoo.http import request
import json
from datetime import date, datetime

def date_handler(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    raise TypeError("Type not serializable")

class PosController(http.Controller):

    @http.route('/api/pos/sessions', type='http', auth='none', methods=['GET'], csrf=False)
    def get_pos_sessions(self, **kwargs):
        try:
            sessions = request.env['pos.session'].sudo().search([])
            sessions_data = []
            for session in sessions:
                session_data = session.read(['name', 'start_at', 'stop_at', 'state', 'user_id', 'config_id'])[0]
                orders = request.env['pos.order'].sudo().search([('session_id', '=', session.id)])
                orders_data = []
                for order in orders:
                    order_data = order.read(['name', 'amount_total', 'date_order', 'lines'])[0]
                    order_lines = []
                    for line in order.lines:
                        order_lines.append({
                            'product_id': line.product_id.id,
                            'product_name': line.product_id.name,
                            'quantity': line.qty,
                            'price_unit': line.price_unit,
                            'discount': line.discount,
                            'price_subtotal': line.price_subtotal,
                            'price_subtotal_incl': line.price_subtotal_incl
                        })
                    order_data['lines'] = order_lines
                    orders_data.append(order_data)
                session_data['orders'] = orders_data
                sessions_data.append(session_data)

            return request.make_response(json.dumps(sessions_data, default=date_handler), 
                                         headers=[('Content-Type', 'application/json')])
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}),
                                         headers=[('Content-Type', 'application/json')], status=500)

    @http.route('/api/pos/sessions/<int:id>/sales', type='http', auth='none', methods=['GET'], csrf=False)
    def get_pos_sales(self, id, **kwargs):
        try:
            session = request.env['pos.session'].sudo().browse(id)
            if not session:
                return request.make_response(json.dumps({'error': 'POS session not found'}),
                                             headers=[('Content-Type', 'application/json')], status=404)
            orders = request.env['pos.order'].sudo().search([('session_id', '=', id)])
            orders_data = []
            for order in orders:
                order_data = order.read(['name', 'amount_total', 'date_order', 'lines'])[0]
                order_lines = []
                for line in order.lines:
                    order_lines.append({
                        'product_id': line.product_id.id,
                        'product_name': line.product_id.name,
                        'quantity': line.qty,
                        'price_unit': line.price_unit,
                        'discount': line.discount,
                        'price_subtotal': line.price_subtotal,
                        'price_subtotal_incl': line.price_subtotal_incl
                    })
                order_data['lines'] = order_lines
                orders_data.append(order_data)

            return request.make_response(json.dumps(orders_data, default=date_handler), 
                                         headers=[('Content-Type', 'application/json')])
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}),
                                         headers=[('Content-Type', 'application/json')], status=500)
