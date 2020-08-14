# -*- encoding: utf-8 -*-
"""
@File    : API_sample_listSubmit.py
@Time    : 2020-08-10 13:42
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
'''用户样本待寄回状态的样本列表'''
import requests,pprint
from config.config import HOSTL,sessionfile
from Lib.Get_read_Excel import read_file
session = read_file(sessionfile)
url = f"{HOSTL}/sample/api/listSubmit"

headers = {'sessionId': session}

response = requests.request("GET", url, headers=headers).json()

pprint.pprint(response)