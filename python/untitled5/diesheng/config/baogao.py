from HTMLTestReportCN import HTMLTestRunner
import unittest
def csbg(test_name,report_path):
    #unittest.main()
    ####生成测试报告#######
    #第一步创建一个测试套件（文件夹）
    suite=unittest.TestSuite()
    #第二步向测试套件里添加测试用例
    # for i in test_name[0]:
    suite.addTest(test_name)
    #第三步将生成的测试结果写入html
    with open(report_path,'wb') as f:
        runner=HTMLTestRunner(
                                stream=f,
                                title='测试报告',
                                description='报告的描述',
                                verbosity=2
        )
        #verbosity 输出内容的详细等级 默认是0,2是最详细
        #执行测试用例，并声称html测试报告
        runner.run(suite)