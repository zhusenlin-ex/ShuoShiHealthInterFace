# -*- encoding: utf-8 -*-
"""
@File    : API_wechat_getSession.py
@Time    : 2020-07-22 14:23
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
'''初始化获取session并存储在文件内'''
import os
import requests
from config.config import HOSTL,sessionfile
from Lib.Write_Excel import write_manage
# 1、获取微信小程序用户信息并且返回session
url = f"{HOSTL}/user/api/wechat/getSession"
querystring = {"type":"0","code":'051wn9000RvP4K10bv200vfFLy4wn90r'}
response = requests.request("GET", url, params=querystring)
newresp = response.json()
if newresp['msg'] == 'OK':
    session = newresp['data']['sessionId']
    write_manage(sessionfile,session)
    print('session已经保存成功')
    # print(session)
else:
    print('code失效了，请更新code')
    os._exit(0) #正常关闭进程

