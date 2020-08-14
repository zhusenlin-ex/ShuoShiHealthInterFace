# -*- encoding: utf-8 -*-
"""
@File    : API_sample_get.py
@Time    : 2020-07-27 16:12
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
'''查看报告信息详情'''
import requests
from config.config import HOSTL,sessionfile
from Lib.WXxiaochengxu.API_sample_list import blist
from Lib.Get_read_Excel import read_file
import pprint
session = read_file(sessionfile)
for one in blist:
    url = f"{HOSTL}/sample/api/get"
    querystring = {"sampleId":one}
    headers = {
        'sessionId': session
        }
    response = requests.request("GET", url, headers=headers, params=querystring).json()

    # pprint.pprint(f'编号：{one},{response.json()}')