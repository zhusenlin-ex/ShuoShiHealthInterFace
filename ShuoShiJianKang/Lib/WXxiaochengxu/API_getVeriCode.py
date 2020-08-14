# -*- encoding: utf-8 -*-
"""
@File    : API_getVeriCode.py
@Time    : 2020-07-22 14:47
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
'''获取样本身份短信验证码'''
from config.config import HOSTL,sessionfile
import requests
from Lib.Get_read_Excel import read_file
import pymysql.cursors
import re
session = read_file(sessionfile)
def get_Vericode(data):
    url = f"{HOSTL}/sample/api/getVeriCode"
    headers = {
        'sessionId': session
        }
    querystring = {"phone": data}
    # json.loads(querystring)
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    # get_session('081zxNaw1gwAMf0T4Cbw1gbMaw1zxNa7')
    return response.json()

# print(querystring,type(querystring))

# 连接数据库
connect = pymysql.Connect(
    host='rm-uf6g9319bt73954u8io.mysql.rds.aliyuncs.com',
    port=3306,
    user='root',
    passwd='sbio&2025',
    db='sssw_message_test',
    charset='utf8'
)

data ='15411111111'
get_Vericode(data)
# 获取游标
cursor = connect.cursor()
# 根据手机号查询信息表中的短信验证码
sql = f"SELECT content FROM sms_record WHERE phone = '{data}'  ORDER BY create_time DESC;"
cursor.execute(sql)
#因为我的sql语句按照倒特定条件，倒序排列，因此第一条符合查询结果
code = cursor.fetchone()
# print(code)
# ('{"code":"482878"}',)
#利用正则表达式将验证码提取出来
res = re.findall('"code":"(.*?)"',code[0])[0]

