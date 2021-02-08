# -*- coding: utf-8 -*-

from odoo import models, _, fields, api
from scripts import utils
class SmartBot(models.AbstractModel):
    # _name = 'smart_bot.smart_bot'
    _inherit = 'mail.bot'
    # _description = 'smart_bot.smart_bot'

    def _get_answer(self, record, body, values, command=False):
        print(record, body, values, command)
        odoobot_state = self.env.user.odoobot_state
        if self._is_bot_in_private_channel(record):
            # main flow
            intent = utils.intent_ext(body)
            if _("hello bot") in body or "hello bot" in body:
                return _("Hello from Ehio Technologies!")
            elif body == "createSale" or  body == "makeSale":
                return _("Kindly provide the details of the sale order")
   
        return super(SmartBot, self)._get_answer(record, body, values, command=False)