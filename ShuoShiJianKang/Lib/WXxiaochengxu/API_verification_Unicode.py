# -*- encoding: utf-8 -*-
"""
@File    : API_verification_Unicode.py
@Time    : 2020-07-28 10:49
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
'''验证一物一码的有效性'''
import requests
from config.config import HOSTL,sessionfile
from Lib.Get_read_Excel import read_file
from config.encryption import get_code
from Lib.WXxiaochengxu.API_Get_Unicode import get_unicode
session = read_file(sessionfile)
def verification_Unicode(code):
    url = f"{HOSTL}/unicode/api/verification"
    querystring = {"uniCode":get_code(code)}
    headers = {
        'sessionId': session
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
# sa = get_unicode()
verification_Unicode(get_unicode('7727e8a29414b4c9c214a9e4e7aa0af2'))