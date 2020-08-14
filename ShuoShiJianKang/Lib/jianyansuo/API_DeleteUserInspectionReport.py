# -*- encoding: utf-8 -*-
"""
@File    : API_DeleteUserInspectionReport.py
@Time    : 2020/6/24 13:38
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
# 删除报告
import requests,json
from config.config import HOST
from config.encryption import get_code
def api_deleteUserInspectionReport(heaData,indata):
    report_url = f'{HOST}/sample/deleteUserInspectionReport'
    header = json.loads(heaData)
    payload ={
    "hosBarCode": get_code(indata)
    }

    reps = requests.delete(report_url,headers = header ,params =payload)
    # print(reps.json())
    return reps.json()


# api_deleteUserInspectionReport('P.URL.CN/0V/L$O*CBI/WJATNX+Y')
#
