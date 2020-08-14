# -*- encoding: utf-8 -*-
"""
@File    : Get_read_Excel.py
@Time    : 2020/6/24 9:30
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""

#---------------python操作excel---------------
#---------------1.读取用例-----参数化---------
#常用的库：openpyxl 、xlrd、xlwt 、xlutils
# exceldir = 'D:\PycharmProjects\ShuoShiJianKang\data\硕世接口测试用例test.xls'
# # print(exceldir)
# #打开excel
# # formatting_info=True (保存原样--样式)不支持xlsx
# workBook = xlrd.open_workbook(exceldir,formatting_info=True)
# sheetNames = workBook.sheet_names()#获取所有的表（sheet）名--列表
# # print(sheetNames)
# # 2-操作对应的用例表（sheet）
# worksheet = workBook.sheet_by_name('获取用户信息')
# #3-读取：一行 一列 单元格
# #1 一行
# # rowData = worksheet.row_values(1)
# # print(rowData)
# # #2-一列
# # colData = worksheet.col_values(0)
# # print(colData)
# # #3-单元格数据
# # cellData = worksheet.cell_value(1,1)
# # print(cellData)
# # ----------------2.写用例----测试结果------------
# # 1- 在缓存里copy一个Excel对象 --不影响源数据用例
# from xlutils.copy import copy
# new_workBook = copy(workBook)#复制出来的新excel对象
# new_workSheet = new_workBook.get_sheet(0)#x新的sheet
# print(new_workSheet)

import xlrd,xlwt
from xlutils.copy import copy
def get_excelData(sheetName,startRow,endRow,heacol,bodyCol,repscol):
    '''
    :param sheetName: 表名
    :param startRow: 开始行数
    :param endRow: 结束函数
    :param heacol: 请求头列数
    :param bodyCol: 请求体列数
    :param repscol: 响应体列数
    :return:
    '''
    # 文件路径
    excelDir = '../data/硕世接口测试用例testV1.2-2020-07-17.xls'
    # 打开excel文件，保持原格式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    # 根据sheet名获取sheet全部内容
    workSheet = workBook.sheet_by_name(sheetName)
    # rowNum = workSheet.nrows
    # colNum = workSheet.ncols
    # print(rowNum,colNum)
    # for one in range (0,rowNum):
    #     data = workSheet.row_values(one)
    #     print(data)
    dataList = []
    for cnt in range(startRow,endRow):
        cellData = workSheet.cell_value(cnt,heacol)#字符串类型 请求头
        bodyData = workSheet.cell_value(cnt,bodyCol)#字符串类型 请求体
        repsCellData = workSheet.cell_value(cnt,repscol)
        dataList.append((cellData,bodyData,repsCellData))
    print(dataList)
    return dataList

# get_excelData('获取用户信息')

def read_file(excelDir):
    '''
    1.copy,f复制excel文件
    2.将测试结果写入excel指定单元格
    :return:
    '''
    # 文件路径
    with open(excelDir,'r',encoding='utf8') as fo:
        a = fo.read()
        return a