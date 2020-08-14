# -*- encoding: utf-8 -*-
"""
@File    : API_sample_list.py
@Time    : 2020-07-27 15:41
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
'''查看报告信息列表'''
import requests
import pprint
from config.config import HOSTL,sessionfile
from Lib.Get_read_Excel import read_file
session = read_file(sessionfile)
url = f"{HOSTL}/sample/api/list"
querystring = {"size":"15","current":"1"}
headers = {
    'sessionId': session
    }
response = requests.request("GET", url, headers=headers, params=querystring)
pprint.pprint(response.json())
# print(response.json())
respnew = response.json()
alist = respnew['data']
# print(alist)
blist = []
for one in alist:
    # print(one['sampleId'],type(one['sampleId']))
    a = one['sampleId']
    blist.append(a)
print(blist)