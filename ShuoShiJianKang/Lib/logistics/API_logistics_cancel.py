# -*- encoding: utf-8 -*-
"""
@File    : API_logistics_cancel.py
@Time    : 2020-07-28 11:17
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
def logistics_Cancel():
    import os
    import requests
    import json
    from config.config import HOSTL,sessionfile,logst
    from Lib.Get_read_Excel import read_file
    session = read_file(sessionfile)
    logisticsid = read_file(logst)

    # 下面两个接口传参相同
    headers = {
        'sessionId': session
        }
    payload = {'logisticsId': logisticsid}
    '''第一步：查询是否可以取消'''
    url = f"{HOSTL}/sample/api/logistics/getCancelFlag"
    response = requests.request("GET", url, data=payload, headers=headers).json()
    # print(response)
    if response['code'] == 0:
        if response['data']['cancelFlag'] == 1:
            '''第二部取消物流'''
            url = f"{HOSTL}/sample/api/logistics/cancel"
            response = requests.request("PUT", url, data=payload, headers=headers)
            if response.json()['code']==0:
                print('取消成功，请去下单')
            else:
                print('取消失败，根据物流编号查询，暂无可退',response.json())
        else:
            print('不能取消')
            os._exit(0)
    else:
        print(response['msg'])
        os._exit(0)
logistics_Cancel()