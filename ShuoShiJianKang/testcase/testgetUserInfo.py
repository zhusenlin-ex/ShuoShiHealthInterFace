# -*- encoding: utf-8 -*-
"""
@File    : testgetUserInfo.py
@Time    : 2020/6/24 9:08
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
import xlrd
from Lib.jianyansuo.Api_getUserInfo import api_getUserInfo
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
    for cnt in range(1,rowNum):
        numData = workSheet.cell_value(cnt,2)
        cellData = workSheet.cell_value(cnt,5)#字符串类型 请求头
        # print(cellData,type(cellData))
        bodyData = workSheet.cell_value(cnt,6)#字符串类型 请求体
        # print(bodyData,type(bodyData))
        repsCellData = workSheet.cell_value(cnt,8)#预期结果返回值
        # print(repsCellData,type(repsCellData))
        # dataList.append((cellData,bodyData,repsCellData))
        res = api_getUserInfo(cellData,bodyData)
        if res['message'] in repsCellData:
            print(f'{numData}----测试通过-----')
            print(res, repsCellData)

        else:
            print(f'{numData}----测试不通过-----')
            print(res,repsCellData)
    # print(dataList)
    # return dataList

get_excelData('获取用户信息')
# @pytest.mark.parametrize('heaData,inData,repsData',get_excelData('获取用户信息'))
# def test_getuser(heaData,inData,repsData):
#     res = api_getUserInfo(heaData,inData)
#     # print(json.loads(res)['message'])
#     # print('-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1')
#     # print(json.loads(repsData)['message'])
#     assert json.loads(res)['message'] in json.loads(repsData)['message']
#
# pytest.main([r'D:\PycharmProjects\ShuoShiJianKang\testcase\testgetUserInfo.py'])
