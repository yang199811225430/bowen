#！/user/bin/python
#-*- coding:utf-8 -*-
# driver 控制回归测试时你需要测试哪些模块就跑哪些模块的脚本
from report.baogao import *
with open(r'F:\学习总结\python\untitled6\driver\a.txt','r')as f:
    a=f.readlines()
    if 'all' in a:
        baogao('*')
    else:
        baogao(a)