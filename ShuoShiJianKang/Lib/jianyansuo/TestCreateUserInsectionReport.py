# -*- encoding: utf-8 -*-
"""
@File    : createUserInspectionReport.py
@Time    : 2020/6/23 9:48
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
import requests,json
import pprint
'''
测试地址：http://testapi.s-sbio.com:9001/sample
正式地址：http://api.s-sbio.com:9001/sample
'''
host = 'http://testapi.s-sbio.com:9001/sample'
'''-------------------------------------------------阴性-------------------------------'''
# 1.阴性报告
# header = {
#     "appKey": "ab99093d26ef45c59eb1cf6bae3a1263",
#     "Content-Type": "application/json;charset=UTF-8 "
# }
# payload = {
#     "hosBarCode": "UC5VUkwuQ04vMEZRUi9MWjYvMEhEMFE3WTMtKg==",
#     "sampleTestNo": "20081109234190",
#     "sampleReceiveTime": "1596422477",
#     "sampleTestTime": "1596422477",
#     "sampleReportTime": "1596422477",
#     "testPeople": "硕世check1号",
#     "reviewPeople": "硕世check2号",
#     "testMethod": "人乳头瘤测试",
#     "sampleType": 36,
#     "sampleStatus": 1,
#     "sampleStatusShow": "合格",
#     "testContent": "人乳头瘤病毒test",
#     "testResult": "人乳头瘤病毒高危型感染",
#     "testItem": [
#         {
#             "subType": "HPV16 ",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV18",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV26",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV31",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV33",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV35",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV39",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV45",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV51 ",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV52",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV53",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV56",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV58",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV59",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV66",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV68",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV73",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV82",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV6",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV11",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV81",
#             "result": 0,
#             "infectUnit": ""
#         },
#     ]
# }

'''----------------------------------阳性----------------------------------'''
# 1.阳性报告
# header = {
#     "appKey": "ab99093d26ef45c59eb1cf6bae3a1263",
#     "Content-Type": "application/json;charset=UTF-8 "
# }
# payload = {
#     "hosBarCode": "UC5VUkwuQ04vMEZRUi9MWjYvMEhEMFE3WTMtKg==",
#     "sampleTestNo": "10000002",
#     "sampleReceiveTime": "1596422477",
#     "sampleTestTime": "1596422477",
#     "sampleReportTime": "1596422477",
#     "testPeople": "硕世check1号",
#     "reviewPeople": "硕世check2号",
#     "testMethod": "人乳头瘤测试",
#     "sampleType": 36,
#     "sampleStatus": 1,
#     "sampleStatusShow": "合格",
#     "testContent": "人乳头瘤病毒test",
#     "testResult": "人乳头瘤病毒高危型感染",
#     "testItem": [
#         {
#             "subType": "HPV16 ",
#             "result": 1,
#             "infectUnit": "87.89%"
#         },
#         {
#             "subType": "HPV18",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV26",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV31",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV33",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV35",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV39",
#             "result": 1,
#             "infectUnit": "92.87%"
#         },
#         {
#             "subType": "HPV45",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV51 ",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV52",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV53",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV56",
#             "result": 1,
#             "infectUnit": "95.24%"
#         },
#         {
#             "subType": "HPV58",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV59",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV66",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV68",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV73",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV82",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV6",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV11",
#             "result": 0,
#             "infectUnit": ""
#         },
#         {
#             "subType": "HPV81",
#             "result": 1,
#             "infectUnit": "87.33%"
#         },
#     ]
# }

'''--------------------------全阳-------------------------'''

header = {
    "appKey": "ab99093d26ef45c59eb1cf6bae3a1263",
    "Content-Type": "application/json;charset=UTF-8 "
}
payload = {
    "hosBarCode": "UC5VUkwuQ04vMEZRUi9MWjYvMEhEMFE3WTMtKg==",
    "sampleTestNo": "20081109234190",
    "sampleReceiveTime": "1596422477",
    "sampleTestTime": "1596422477",
    "sampleReportTime": "1596422477",
    "testPeople": "硕世check1号",
    "reviewPeople": "硕世check2号",
    "testMethod": "人乳头瘤测试",
    "sampleType": 36,
    "sampleStatus": 1,
    "sampleStatusShow": "合格",
    "testContent": "人乳头瘤病毒test",
    "testResult": "人乳头瘤病毒高危型感染",
    "testItem": [
        {
            "subType": "HPV16 ",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV18",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV26",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV31",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV33",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV35",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV39",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV45",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV51 ",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV52",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV53",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV56",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV58",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV59",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV66",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV68",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV73",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV82",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV6",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV11",
            "result": 1,
            "infectUnit": ""
        },
        {
            "subType": "HPV81",
            "result": 1,
            "infectUnit": ""
        },
    ]
}

res = requests.post(url= f'{host}/createUserInspectionReport',headers=header,json =payload)
pprint.pprint(res.json())