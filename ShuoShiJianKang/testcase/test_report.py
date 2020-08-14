# -*- encoding: utf-8 -*-
"""
@File    : test_report.py
@Time    : 2020-06-28 13:28
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
import xlrd
from xlutils.copy import copy
from Lib.jianyansuo.Api_createUserInspectionReport import api_createUserInspectionReport
def get_excelData(sheetName):
    '''
    :param sheetName: 表名
    :param startRow: 开始行数
    :param endRow: 结束函数
    :param heacol: 请求头列数
    :param bodyCol: 请求体列数
    :param repscol: 响应体列数
    :return:
    '''
    excelDir = '../data/硕世接口测试用例test.xls'
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    workSheet = workBook.sheet_by_name(sheetName)
    rowNum = workSheet.nrows
    colNum = workSheet.ncols
    # print(rowNum,colNum)
    # dataList = []
    new_workbook = copy(workBook)
    new_worrsheet = new_workbook.get_sheet(1)
    for cnt in range(1,rowNum):
        numData = workSheet.cell_value(cnt,2)
        cellData = workSheet.cell_value(cnt,5)#字符串类型 请求头
        # print(cellData,type(cellData))
        bodyData = workSheet.cell_value(cnt,6)#字符串类型 请求体
        # print(bodyData,type(bodyData))
        repsCellData = workSheet.cell_value(cnt,8)#预期结果返回值
        # print(repsCellData,type(repsCellData))
        # dataList.append((cellData,bodyData,repsCellData))
        res = api_createUserInspectionReport(cellData,bodyData)
        if res['message'] in repsCellData:
            # print(f'{numData}----测试通过-----')
            # print(res, repsCellData)
            info = 'pass'

        else:
            # print(f'{numData}----测试不通过-----')
            # print(res,repsCellData)
            info = 'fail'
        new_worrsheet.write(cnt, 9, res)
        new_worrsheet.write(cnt,10,info)
        print(f'{numData}----测试完成，结果以写入-----')
    new_workbook.save(r'./res.xls')
    # print(dataList)
    # return dataList
get_excelData('推送用户报告信息')