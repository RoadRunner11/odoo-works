#!/usr/bin/env python

# coding: utf-8

import xmlrpc.client as xc

# import xlrd

dbname = 'odoo13'

username = 'admin'

pwd = 'admin'

sock_common = xc.ServerProxy ('http://18.216.227.139:8069/xmlrpc/2/common')

sock = xc.ServerProxy('http://18.216.227.139:8069/xmlrpc/object')

uid = sock_common.authenticate(dbname, username, pwd, {})

def create_order():
	account_ids = sock.execute(dbname, uid, pwd, 'sale.order', 'create', 
					{   'name': 'fist_order',
						'partner_id': 1, 'pricelist_id':1
						})

	return "Sale Order Created Successfully...!"