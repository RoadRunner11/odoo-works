# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pos_receipt_customer_name(models.Model):
#     _name = 'pos_receipt_customer_name.pos_receipt_customer_name'
#     _description = 'pos_receipt_customer_name.pos_receipt_customer_name'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
