# -*- coding: utf-8 -*-
import json
import base64
import pyqrcode

__author__ = ['Yiwei Huang']


config_f = 'ssconfig.txt'

# ss://method:password@hostname:port
cf = open(config_f, 'r', encoding='utf-8')
parameter = json.load(cf)
head = 'ss://'
method = str(parameter['method'])#'AES-256-CFB'
password = str(parameter['password'])
hostname = parameter['server']
port     = str(parameter['server_port'])
uri = method+':'+password+'@'+hostname+':'+port
uri_base64 = head+base64.b64encode(bytes(uri,'utf-8')).decode('utf-8')
cf.close()

#%% QR code
q = pyqrcode.create(uri_base64)
q.png('ssqrcode.png',scale=15)
