# -*- coding: utf-8 -*-
# from odoo import http


# class SmartBot(http.Controller):
#     @http.route('/smart_bot/smart_bot/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_bot/smart_bot/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_bot.listing', {
#             'root': '/smart_bot/smart_bot',
#             'objects': http.request.env['smart_bot.smart_bot'].search([]),
#         })

#     @http.route('/smart_bot/smart_bot/objects/<model("smart_bot.smart_bot"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_bot.object', {
#             'object': obj
#         })
