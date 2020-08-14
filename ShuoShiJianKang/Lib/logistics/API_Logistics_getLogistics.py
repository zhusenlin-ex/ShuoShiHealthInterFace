# -*- encoding: utf-8 -*-
"""
@File    : API_Logistics_getLogistics.py
@Time    : 2020-07-29 14:32
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
def logistics_getLogistics():
    import requests
    import json,pprint
    from config.config import HOSTL, sessionfile, logst
    from Lib.Get_read_Excel import read_file
    from Lib.Write_Excel import write_manage
    logisticsid = read_file(logst)
    session = read_file(sessionfile)
    url = f"{HOSTL}/sample/api/logistics/getLogistics"
    payload = {"logisticsId":logisticsid}
    headers = {'sessionId': session}
    response = requests.request("GET", url, data=payload, headers=headers).json()
    pprint.pprint(response)



if __name__ == '__main__':
    logistics_getLogistics()