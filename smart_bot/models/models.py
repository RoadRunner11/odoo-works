# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SmartBot(models.AbstractModel):
    # _name = 'smart_bot.smart_bot'
    _inherit = 'mail.bot'
    # _description = 'smart_bot.smart_bot'

    def _get_answer(self, record, body, values, command=False):
        
        odoobot_state = self.env.user.odoobot_state
        if self._is_bot_in_private_channel(record):
            # main flow
            if "hello bot" in body:
                return _("Hello from Ehio Technologies!")
        return super(SmartBot, self)._get_answer(record, body, values, command=False)
