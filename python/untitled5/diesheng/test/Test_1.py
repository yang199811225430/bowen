from HTMLTestReportCN import HTMLTestRunner
import unittest
from time import *
from appium import webdriver
import warnings
from diesheng.config import duqu
from diesheng.config import baogao
from diesheng.config.config_3 import get_logger
log=get_logger('test_1')
class TC(unittest.TestCase):
    #每个用例执行之前运行一次，用于清理测试环境的残留数据
    def setUp(self):
        self.des = {"platformName": "Android",
                       "platformVersion": "5.1.1",
                       "deviceName": "emulator-5554",
                       "appPackage": "com.qk.butterfly",
                       "appActivity": ".main.LauncherActivity",
                       "unicodeKeyboard": "True",
                       "resetKeyboard": "True",
                       "noReset": "true"
                       }
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5)
        log.info('手机与appuim成功建立连接')
    #开始写测试 用例
    def test_1(self):
        # 使用账号密码登录
        #
        log.info('点击密码按键，进入账号密码登录界面')
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        for i in duqu.read_data():
            self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(i[0])
            log.info(f'输入的手机号是：{i[0]}')
            self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(i[1])
            log.info(f'输入的密码是：{i[1]}')
            self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        #断言
            sleep(2)
        #进入登录页面之后，
        #if else 处理登录成功与失败，可以用 try except语句
            try:
                log.info('登录失败的处理')
                b = self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').text
                self.assertEqual(b, '登录', msg='断言登录失败')
            except:
                a = self.dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[-1].text
                self.assertEqual(a, '我的', msg='断言已经登录成功')
                log.info('登录成功的处理')
    #def test_2(self):
    #         b = self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').text
    #         self.assertEqual(b, '登录', msg='断言登录失败')
    #         print('登录失败')
    # def test_3(self):
    #         b = self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').text
    #         self.assertEqual(b, '登录', msg='断言登录失败')
    #         print('登录失败')
    # def test_4(self):
    #         a = self.dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[-1].text
    #         self.assertEqual(a, '我的', msg='断言已经登录成功')
    #         print('登录成功')
    #每个测试用例执行完毕之后，运行teardown一次  作用：测试用例运行完之后，清理测试环境
    def tearDown(self):
        log.info('手机与appium断开连接')
        self.dr.quit()
if __name__ == '__main__':
    # unittest.main()
    baogao.csbg(test_name=TC('test_1'),report_path=r'F:\学习总结\python\untitled5\diesheng\report\a.html')