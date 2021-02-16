-*- coding: utf-8 -*-
import logging
import pprint
import requests
import werkzeug

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class YocoController(http.Controller):
    @http.route('/yoco_payments_acquirer/yoco_payments_acquirer/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/yoco_payments_acquirer/yoco_payments_acquirer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yoco_payments_acquirer.listing', {
#             'root': '/yoco_payments_acquirer/yoco_payments_acquirer',
#             'objects': http.request.env['yoco_payments_acquirer.yoco_payments_acquirer'].search([]),
#         })

#     @http.route('/yoco_payments_acquirer/yoco_payments_acquirer/objects/<model("yoco_payments_acquirer.yoco_payments_acquirer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yoco_payments_acquirer.object', {
#             'object': obj
#         })
