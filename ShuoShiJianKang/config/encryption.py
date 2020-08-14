# -*- encoding: utf-8 -*-
"""
@File    : encryption.py
@Time    : 2020/6/23 16:39
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
import base64
import re

def get_code(indata):
    #加密（编码）
    pwd = base64.b64encode(indata.encode("UTF-8"))
    #byte类型转为str类型，并且将前后引号去除
    forma = str(pwd)[2:-1]
    print(forma)
    return forma




# indata = 'P.URL.CN/0Q%L$BP4-J:G3I%BLV:'
get_code('P.URL.CN/0FQR/LZ6/0HD0Q7Y3-*')