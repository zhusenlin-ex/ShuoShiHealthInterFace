# -*- encoding: utf-8 -*-
"""
@File    : Write_Excel.py
@Time    : 2020-07-03 13:01
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
import xlutils,xlrd,xlwt,os

def write_manage(excelDir,indata):

    with open(excelDir,'w',encoding='utf8') as fo:
        fo.write(indata)




# excelDir = '../data/硕世接口测试用例test.xls'