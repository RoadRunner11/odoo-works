# -*- coding: utf-8 -*-

from odoo import models, _, fields, api
from .utils import intent_ext, add_sale_info
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
			intent = ''
			if odoobot_state == "start":
				intent = intent_ext(body)
			if odoobot_state == 'idle' and _("hello bot") in body or "hello bot" in body:
				self.env.user.odoobot_state = "start"
				return _("Hello from Ehio Technologies!")
			if intent == "createSale":
				self.env.user.odoobot_state = "createSale"
				return _("Kindly provide the details of the sale order, in the formate name, partner id and pricelist id")
			if odoobot_state == 'createSale':
				context = {"name":'', 'partner_id': "", 'pricelist_id':"" }
				return add_sale_info(body, context, self)

			elif odoobot_state == 'getSale':
				return _("Do you want to a sale record")

		return super(SmartBot, self)._get_answer(record, body, values, command=False)