from odoo import http
from odoo.http import request


class VehicleController(http.Controller):

    @http.route('/vehicle/form', auth='public', type='http')
    def vehicle_form(self):
        return request.render('odoo_owl_v15.car_id', {})
