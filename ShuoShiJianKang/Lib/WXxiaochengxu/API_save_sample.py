# -*- encoding: utf-8 -*-
"""
@File    : API_save_sample.py
@Time    : 2020-07-27 14:45
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
import requests
from config.config import HOSTL,sessionfile
from config.encryption import get_code
from Lib.Get_read_Excel import read_file
from Lib.WXxiaochengxu.API_getVeriCode import res
import json
session = read_file(sessionfile)
url = f"{HOSTL}/sample/api/save"
barCode = 'P.URL.CN/0P$N*4B91XDA.N4X4E6'
payload = {
    "barCode":get_code(barCode),
    "name":"测试用户",
    "phone":"15411111111",
    "veriCode":res,
    "cardNo":"13010219900307213X",
    "collectionTime":"1595904030"
    }


headers = {
    'Content-Type': "application/json;charset=UTF-8",
    'sessionId': session
    }

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

print(response.json())