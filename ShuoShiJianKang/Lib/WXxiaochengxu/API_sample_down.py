# -*- encoding: utf-8 -*-
"""
@File    : API_sample_down.py
@Time    : 2020-07-27 16:34
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
'''下载样本报告'''
import requests
from config.config import HOSTL,sessionfile
from Lib.WXxiaochengxu.API_sample_list import blist
from Lib.Get_read_Excel import read_file
session = read_file(sessionfile)
for one in blist:
    url = f"{HOSTL}/sample/api/download"
    querystring = {"sampleId":one}
    headers = {
        'sessionId': session
        }
    response = requests.request("GET", url, headers=headers, params=querystring).content
    with open(f'./sample_report/{one}.pdf','wb') as foo:
        # print(f'当前正在下载{one}')
        foo.write(response)
        # print(f'{one}以下载完成')
    # print(response.text)