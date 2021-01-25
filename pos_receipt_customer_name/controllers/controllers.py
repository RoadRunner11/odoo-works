# -*- coding: utf-8 -*-
# from odoo import http


# class PosReceiptCustomerName(http.Controller):
#     @http.route('/pos_receipt_customer_name/pos_receipt_customer_name/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_receipt_customer_name/pos_receipt_customer_name/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_receipt_customer_name.listing', {
#             'root': '/pos_receipt_customer_name/pos_receipt_customer_name',
#             'objects': http.request.env['pos_receipt_customer_name.pos_receipt_customer_name'].search([]),
#         })

#     @http.route('/pos_receipt_customer_name/pos_receipt_customer_name/objects/<model("pos_receipt_customer_name.pos_receipt_customer_name"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_receipt_customer_name.object', {
#             'object': obj
#         })
