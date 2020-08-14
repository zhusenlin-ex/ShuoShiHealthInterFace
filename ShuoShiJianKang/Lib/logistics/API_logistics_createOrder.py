# -*- encoding: utf-8 -*-
"""
@File    : API_logistics_createOrder.py
@Time    : 2020-07-28 10:59
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
def logistics_createOrder():
    import re,os
    import requests,time
    import json
    from config.config import HOSTL,sessionfile,logst
    from Lib.Get_read_Excel import read_file
    from Lib.Write_Excel import write_manage
    session = read_file(sessionfile)
    url = f"{HOSTL}/sample/api/logistics/createOrder"
    timenum = int(time.time())
    payload = {
        "startContactName":"朱森林",
        "startContactPhone":"17349766478",
        "startStationAddress":"上海市松江区泗泾镇鼓楼公路1899弄36号801室，来的时候请提前打我电话或者在门卫门口等我",
        "orderEtd":timenum,
        "sampleIds":"3"
        }
    headers = {
        'Content-Type': "application/json",
        'sessionId': session,
        }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    # print(response.json())
    if response.json()['code'] == 0:
        logisticsid = response.json()['data']['logisticsId']
        write_manage(logst,str(logisticsid))
        print('创建物流订单成功，物流号为：%s'%(logisticsid))
    else:
        print('重复下单，请先去取消订单')
        os._exit(0)
    print(logisticsid)
    import time
    print(int(time.time()))