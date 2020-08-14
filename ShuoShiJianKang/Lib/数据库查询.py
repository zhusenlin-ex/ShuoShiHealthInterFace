# -*- encoding: utf-8 -*-
"""
@File    : 数据库查询.py
@Time    : 2020-08-12 10:21
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
import pprint
import  pymysql.cursors
# 数据库连接配置
connect = pymysql.Connect(
    host='rm-uf6g9319bt73954u8io.mysql.rds.aliyuncs.com',
    port=3306,
    user='root',
    passwd='sbio&2025',
    db='pre_sssw',
    charset='utf8'
)
# 建立游标
cursor = connect.cursor()

# 编写sql脚本语句
sql = "select * from sample_info  order by create_time desc"
# 执行语句
cursor.execute(sql)
# 检索所有结果
res = cursor.fetchall()
# 按照每一条打印行数据
for i in res:
    print(i)
# 关闭游标
cursor.close()