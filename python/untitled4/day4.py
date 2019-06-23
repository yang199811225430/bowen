#unittest 单元测试
import HTMLTestReportCN
import unittest

# class T(unittest.TestCase):
#     def test_1(self):
#         #预期结果
#         x='宝马'
#         #实际结果
#         y='自行车'
#         #第一个断言的方法,判断预期结果与实际结果是否相等
#         self.assertEqual(x,y,msg='msg的作用就是填写备注信息')
#
#     def test_2(self):
#         # 预期结果
#         x = '自行车'
#         # 实际结果
#         y = '自行车'
#         # 第一个断言的方法,判断预期结果与实际结果是否相等
#         self.assertEqual(x, y, msg='msg的作用就是填写备注信息')
# if __name__ == '__main__':
#     #unittest.main()
#     ####生成测试报告#######
#     #第一步创建一个测试套件（文件夹）
#     suite=unittest.TestSuite()
#     #第二步向测试套件里添加测试用例
#     suite.addTest(T('test_1'))
#     suite.addTest(T('test_2'))
#     #第三步将生成的测试结果写入html
#     with open('a.html','wb') as f:
#         runner=HTMLTestReportCN.HTMLTestRunner(
#                                                 stream=f,
#                                                 title='测试报告',
#                                                 description='报告的描述',
#                                                 verbosity=2
#         )
#         #verbosity 输出内容的详细等级 默认是0,2是最详细
#         #执行测试用例，并声称html测试报告
#         runner.run(suite)
