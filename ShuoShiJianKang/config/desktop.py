# -*- encoding: utf-8 -*-
"""
@File    : desktop.py
@Time    : 2020-08-13 12:57
@Author  : Forest
@Email   : 17349766478@163.com
@Software: PyCharm
"""
import base64
from tkinter import *
from tkinter import messagebox # python3.0的messagebox，属于tkinter的一个组件

def get_code(indata):
    #加密（编码）
    pwd = base64.b64encode(indata.encode("UTF-8"))
    #byte类型转为str类型，并且将前后引号去除
    forma = str(pwd)[2:-1]
    # print(forma)
    return forma

#窗口创建
top = Tk()#创建tk对象
top.title("硕世自动化-Python-二维码加密系统")#标题
# top.iconbitmap(r'G:\333.ico')
top.geometry('300x150')  # 是x 不是*   框大小

#输入框创建
text = Label(top, text="输入28位二维码")
text.pack(side=TOP)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
xls_text = StringVar()#获取输入
xls = Entry(top, textvariable = xls_text)#输入控件；用于显示简单的文本内容
xls_text.set(" ")#设置默认的内容
xls.pack()#包装

def click():
    message = get_code(xls_text.get().strip())
    messagebox._show(title='加密结果：', message=message)

#包装一个按钮
Button(top, text="加密！", fg="blue", bd=2, width=6, command=click).pack()
#运行
top.mainloop()



