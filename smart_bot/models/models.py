# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SmartBot(models.Model):
    _name = 'smart_bot.smart_bot'
    _inherit = 'mail.bot'
    _description = 'smart_bot.smart_bot'

    def _get_answer(self, record, body, values, command=False):
        print("how are u dear")
        odoobot_state = self.env.user.odoobot_state
        if self._is_bot_in_private_channel(record):
            # main flow
            if _('hello bot') in body or "hello bot" in body:
                return _("Hello from Ehio Technologies!")
        return super(SmartBot, self)._get_answer(record, body, values, command=False)
