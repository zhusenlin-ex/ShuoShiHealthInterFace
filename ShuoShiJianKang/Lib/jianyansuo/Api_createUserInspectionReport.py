# -*- encoding: utf-8 -*-
"""
@File    : Api_createUserInspectionReport.py
@Time    : 2020/6/23 17:02
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
import requests,json
from config.config import HOST
from config.encryption import get_code
import  time
now_time = time.time()
# print(now_time)
import random

# def api_createUserInspectionReport(indata):
#     '''
#     :param indata:
#     :return:
#     '''
#     report_url = f'{HOST}/sample/createUserInspectionReport'
#     header = {
#         "appKey": "ab99093d26ef45c59eb1cf6bae3a1263",
#         "Content-Type": "application/json;charset=UTF-8 "
#     }
#     data ={
#     "hosBarCode": get_code(indata),
#     "sampleTestNo": f"1000000{random.randint(1,1000)}",
#     "sampleReceiveTime": now_time,
#     "sampleTestTime": now_time,
#     "sampleReportTime": now_time,
#     "testPeople": "checkname3",
#     "reviewPeople": "checkname4",
#     "testMethod": "人乳头瘤测试0628",
#     "sampleType": 36,
#     "sampleStatus": 1,
#     "sampleStatusShow": "合格",
#     "testContent": "人乳头瘤病毒test0628",
#     "testResult": "人乳头瘤病毒高危型感染0628",
#     "testItem": [
#         {
#             "subType": "Hpv16",
#             "result": "阳性",
#             "infectUnit": "92.16（11.59%）"
#         },
#         {
#             "subType": "Hpv16",
#             "result": "阳性",
#             "infectUnit": "92.16（11.59%）"
#         }
#     ]
# }
#
#     reps = requests.post(report_url,headers = header ,data=json.dumps(data))
#     print(reps.json())
#     return reps.json()
#
# api_createUserInspectionReport('P.URL.CN/0+:IXDRUT/GF21DR$XA')


# 推送/修改用户报告
def api_createUserInspectionReport(heaDerData,inData):
    '''
    :param indata:
    :return:
    '''

    # print(heaDerData,inData)
    report_url = f'{HOST}/sample/createUserInspectionReport'
    header = json.loads(heaDerData)
    # data = json.loads(inData)
    # payload = {
    #     'hosBarCode': get_code(inData)
    # }
    # print(type(header),type(data))
    reps = requests.post(report_url,headers = header ,json=inData)
    print(reps.json())
    return reps.json()


# api_createUserInspectionReport('{"appKey":"ab99093d26ef45c59eb1cf6bae3a1263"}','P.URL.CN/0P$9HBPIHQ6QDO0FSF.')