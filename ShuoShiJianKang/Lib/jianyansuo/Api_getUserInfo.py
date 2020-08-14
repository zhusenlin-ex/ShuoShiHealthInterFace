# -*- encoding: utf-8 -*-
"""
@File    : Api_getUserInfo.py
@Time    : 2020/6/23 15:44
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
# 获取用户信息
import requests
import json
from config.config import HOST
from config.encryption import get_code
import pprint
def api_getUserInfo(heaData,inData):
    '''
    :param heaData:
    :param inData:
    :return:
    '''
    #1-1接口地址
    info_url = f'{HOST}/sample/getUserInfo'
    #1-2请求头（取自sssw_app表，唯一标识）
    header = json.loads(heaData)
    payload = {
        'hosBarCode': get_code(inData)
    }
    # print(payload)
    reps = requests.get(info_url,headers = header,params = payload).json()
    # pprint.pprint(reps)
    return reps

# api_getUserInfo('{"appKey":"ab99093d26ef45c59eb1cf6bae3a1263"}','P.URL.CN/0P$9HBPIHQ6QDO0FSF.')