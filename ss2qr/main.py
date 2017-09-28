# -*- coding: utf-8 -*-
import os
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
hostname = parameter['server']
password = str(parameter['password'])
port     = str(parameter['server_port'])
uri = method+':'+password+'@'+hostname+':'+port
uri_base64 = head+base64.b64encode(bytes(uri,'utf-8')).decode('utf-8')

#%% QR code
q = pyqrcode.create(uri_base64)
q.png('ssqrcode.png',scale=15)

ter_cmd = 'sudo sserver -p ' + str(parameter['server_port']) +' -k ' + parameter['password'] +' -m rc4-md5 -d start'
os.system(ter_cmd)
