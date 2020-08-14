# -*- encoding: utf-8 -*-
"""
@File    : API_sample_GetSubmitFlag.py
@Time    : 2020-07-27 17:36
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
def sample_listSubmit():
    '''查看用户是否有待回寄的样本，0表示没有，1表示有"待回寄"'''
    import requests
    import pprint
    from config.config import HOSTL,sessionfile
    from Lib.Get_read_Excel import read_file
    session = read_file(sessionfile)
    url = f"{HOSTL}/sample/api/listSubmit"
    headers = {
        'sessionId': session
        }
    response = requests.request("GET", url, headers=headers)
    # print(response.json())
    pprint.pprint(response.json())

if __name__ == '__main__':
    sample_listSubmit()