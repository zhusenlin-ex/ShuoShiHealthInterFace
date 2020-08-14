# -*- encoding: utf-8 -*-
"""
@File    : API_Get_Unicode.py
@Time    : 2020-07-28 10:35
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
'''获取28位一物一码'''
def get_unicode(codeticket):
    import os
    import requests
    from config.config import HOSTL,sessionfile
    from Lib.Get_read_Excel import read_file
    session = read_file(sessionfile)
    url = f"{HOSTL}/unicode/api/get"
    querystring = {"codeTicket":codeticket}
    headers = {
        'sessionId': session
        }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    if response['code'] == 0:
        unicode = response['data']
        # print(unicode)
        return unicode
    else:
        print(response['msg'])
        os._exit(0)
    # print(response)
    # return response.json()



if __name__ == '__main__':

    get_unicode('7727e8a29414b4c9c214a9e4e7aa0af2')