# -*- encoding: utf-8 -*-
"""
@File    : API_logistics_getLatelyLogistics.py
@Time    : 2020-08-10 11:16
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
def logistics_getLatelyLogistics():
    '''获取最新寄件人信息'''
    import requests
    import json, pprint
    from config.config import HOSTL, sessionfile, logst
    from Lib.Get_read_Excel import read_file
    # from Lib.Write_Excel import write_manage

    # logisticsid = read_file(logst)
    session = read_file(sessionfile)
    url = f"{HOSTL}/sample/api/logistics/getLatelyLogistics"
    # payload = {"logisticsId": logisticsid}
    headers = {'sessionId': session}
    response = requests.request("GET", url, headers=headers).json()
    pprint.pprint(response)

if __name__ == '__main__':
    logistics_getLatelyLogistics()