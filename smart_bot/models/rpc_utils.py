#!/usr/bin/env python

# coding: utf-8

import xmlrpc.client as xc
import json
# import xlrd
with open('env.json', 'r') as env_file:
	env_data = json.dumps(env_file)
print(env_data)
server = "http://52.14.87.243:8069/"
dbname = 'odoo13'

username = 'admin'

pwd = 'admin'

sock_common = xc.ServerProxy ('{}/xmlrpc/2/common'.format(server))

sock = xc.ServerProxy('{}/xmlrpc/object'.format(server))

uid = sock_common.authenticate(dbname, username, pwd, {})

def create_order(context):
	account_ids = sock.execute(dbname, uid, pwd, 'sale.order', 'create', 
					{   'name': context["name"],
						'partner_id': context["partner_id"],
						'pricelist_id':context["pricelist_id"]
						})

	return "Sale Order Created Successfully...!"