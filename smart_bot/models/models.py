# -*- coding: utf-8 -*-

from odoo import models, _, fields, api
from .utils import intent_ext
import logging

_logger = logging.getLogger(__name__)
class SmartBot(models.AbstractModel):
    # _name = 'smart_bot.smart_bot'
    _inherit = 'mail.bot'
    # _description = 'smart_bot.smart_bot'

    def _get_answer(self, record, body, values, command=False):
        _logger.debug(record, body, values)
        odoobot_state = self.env.user.odoobot_state
        if self._is_bot_in_private_channel(record):
            # main flow
            intent = intent_ext(body)
            if _("hello bot") in body or "hello bot" in body:
                return _("Hello from Ehio Technologies!")
            elif intent == "createSale" or  intent == "makeSale":
                return _("Kindly provide the details of the sale order")
   
        return super(SmartBot, self)._get_answer(record, body, values, command=False)