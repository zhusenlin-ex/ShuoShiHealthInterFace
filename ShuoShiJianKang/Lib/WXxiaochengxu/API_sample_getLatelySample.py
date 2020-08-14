# -*- encoding: utf-8 -*-
"""
@File    : API_sample_getLatelySample.py
@Time    : 2020-08-10 13:33
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
'''查看当前用户是否绑定样本'''
import requests
import json, pprint
from config.config import HOSTL, sessionfile, logst
from Lib.Get_read_Excel import read_file
session = read_file(sessionfile)
url = f"{HOSTL}/sample/api/getLatelySample"
headers = {'sessionId': session}

response = requests.request("GET", url, headers=headers).json()
pprint.pprint(response)
