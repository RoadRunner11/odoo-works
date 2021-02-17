# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from hashlib import md5
from werkzeug import urls

from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare
# from odoo.addons.payment_alipay.controllers.main import AlipayController
from odoo.addons.payment.models.payment_acquirer import ValidationError

_logger = logging.getLogger(__name__)


class PaymentAcquirerYoco(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('yoco', 'Yoco')])#, ondelete={'yoco': 'set default'})
    # yoco_merchant_id = fields.Char(string="Yoco Merchant ID", required_if_provider='yoco', groups='base.group_user')
    yoco_pub_key = fields.Char(string="Yoco Pub ID", required_if_provider='yoco', groups='base.group_user')
    yoco_sec_key = fields.Char(string="Yoco Sec Key", required_if_provider='yoco', groups='base.group_user')

    def _get_yoco_urls(self, environment):
        """ PayUlatam URLs"""
        if environment == 'prod':
            return 'https://online.yoco.com/v1/charges/'
        return 'https://online.yoco.com/v1/charges/'
    

class PaymentTransactionYoco(models.Model):
    _inherit = 'payment.transaction'

    payload = {
            'APIKEY': self.acquirer_id.yoco_secret_key,
            'txref': self.reference,
        }
    headers = {
        'Content-Type': 'application/json',
    }
