#！/user/bin/python
#-*- coding:utf-8 -*-
from HTMLTestReportCN import HTMLTestRunner
import unittest
def baogao(name):
    #创建一个测试套件
    suite=unittest.TestSuite()
    for i in name:
    #将某一个类中的测试用例添加到测试用例
    #第一个参数 存放测试脚本的路径
    #第二个参数是匹配测试文件的通配符
    #自动去发现符合通配符文件中以test开头的函数，提取出来放在discover中  结果是个列表
        discover=unittest.defaultTestLoader.discover(r'F:\学习总结\python\untitled6\test\biek_test',pattern='{}_test.py'.format(i.strip()))
        for j in discover:
            suite.addTest(j)
    with open(r'F:\学习总结\python\untitled6\report\abc.html','wb') as f:
        runner=HTMLTestRunner(
                                stream=f,
                                tester='ycx',
                                title='别克测试报告',
                                description='报告的描述',
                                verbosity=2
        )
        #verbosity 输出内容的详细等级 默认是0,2是最详细
        #执行测试用例，并声称html测试报告
        runner.run(suite)