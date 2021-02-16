# -*- coding: utf-8 -*-
# from odoo import http


# class PaymentYoco(http.Controller):
#     @http.route('/payment_yoco/payment_yoco/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment_yoco/payment_yoco/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment_yoco.listing', {
#             'root': '/payment_yoco/payment_yoco',
#             'objects': http.request.env['payment_yoco.payment_yoco'].search([]),
#         })

#     @http.route('/payment_yoco/payment_yoco/objects/<model("payment_yoco.payment_yoco"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment_yoco.object', {
#             'object': obj
#         })
