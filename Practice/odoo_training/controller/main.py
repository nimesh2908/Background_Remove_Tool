from odoo import http
from odoo.http import request

class Main(http.Controller):

    @http.route('/car_details', type='http', auth='public', website=True)
    def car_details(self, **post):
        res = request.env['car'].search([])
        for record in res:
            print(record)
        return request.render('odoo_training.car_template',{'result':res})
