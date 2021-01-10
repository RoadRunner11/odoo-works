# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SmartBot(models.Model):
    _name = 'smart_bot.smart_bot'
    _inherit = 'mail.bot'
    _description = 'smart_bot.smart_bot'

    def _get_answer(self, record, body, values, command=False):
        # onboarding
        odoobot_state = self.env.user.odoobot_state
        if self._is_bot_in_private_channel(record):
            # main flow
            if odoobot_state == 'onboarding_emoji' and self._body_contains_emoji(body):
                self.env.user.odoobot_state = "onboarding_attachement"
                return _("Great! 👍<br/>Now, try to <b>send an attachment</b>, like a picture of your cute dog...")
