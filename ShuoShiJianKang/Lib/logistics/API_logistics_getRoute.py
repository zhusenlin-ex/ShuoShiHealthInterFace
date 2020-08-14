# -*- encoding: utf-8 -*-
"""
@File    : API_logistics_getRoute.py
@Time    : 2020-07-28 13:53
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
'''查看物流动态'''
def logistics_getRoute():
    import requests
    import os
    import json
    from config.config import HOSTL,sessionfile,logst
    from Lib.Get_read_Excel import read_file
    session = read_file(sessionfile)
    logisticsid = read_file(logst)
    url = f"{HOSTL}/sample/api/logistics/getRoute"
    payload = {'logisticsId': logisticsid}
    headers = {
        'sessionId': session
        }
    response = requests.request("GET", url, data=payload, headers=headers).json()
    print(response['data'][0])

if __name__ == '__main__':
    logistics_getRoute()