# -*- encoding: utf-8 -*-
"""
@File    : test_runner.py
@Time    : 2020-06-28 15:19
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
import pytest
import allure
import os
from Lib.Get_read_Excel import get_excelData
from Lib.jianyansuo.Api_getUserInfo import api_getUserInfo
from Lib.jianyansuo.Api_createUserInspectionReport import api_createUserInspectionReport
from Lib.jianyansuo.API_DeleteUserInspectionReport import api_deleteUserInspectionReport
@allure.feature('接口集')
@allure.severity("normal")
# @pytest.mark.user_info(order = 2)
class TestZuser_info:
    @allure.story("01检验所查询用户信息")
    @allure.title("查询用户信息用例")
    @pytest.mark.user_info_select
    @pytest.mark.parametrize('inData,twData,repsData',get_excelData('001检验所接口',1,9,5,6,8))
    def test_chaxun_report(self,inData,twData,repsData):
        res = api_getUserInfo(inData,twData)
        assert res['message'] in repsData

    @allure.story("02推送报告信息")
    @allure.title("推送报告")
    @pytest.mark.user_info_select
    @pytest.mark.parametrize('inData,twData,repsData', get_excelData('001检验所接口', 10, 26, 5, 6, 8))
    def test_add_report(self, inData, twData, repsData):
        res = api_createUserInspectionReport(inData, twData)
        assert res['message'] in repsData

    @allure.story("特殊情况下-删除报告信息")
    @allure.title("删除报告")
    @pytest.mark.user_info_select
    @pytest.mark.parametrize('inData,twData,repsData', get_excelData('001检验所接口', 27, 35, 5, 6, 8))
    def test_delete_report(self, inData, twData, repsData):
        res = api_deleteUserInspectionReport(inData, twData)
        assert res['message'] in repsData

if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /tmp 目录
    pytest.main(['test_runner.py', '-s', '--alluredir', '../report/tmp'])
    # 执行命令 allure generate ./tmp -o ./report --clean ，生成测试报告
    os.system('allure generate  ../Report/tmp -o ../Report/report --clean')

