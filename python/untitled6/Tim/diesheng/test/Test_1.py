from HTMLTestReportCN import HTMLTestRunner
import unittest
from time import *
from appium import webdriver
import warnings
from Tim.diesheng.config import duqu
from Tim.diesheng.config import baogao
from Tim.diesheng.config.config_3 import get_logger
log=get_logger('Test_1')
class TC(unittest.TestCase):
    @classmethod
    def setUpClass(self):
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
        log.info('点击密码按键，进入账号密码登录界面')
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(17637839607)
        log.info(f'输入的手机号是：{17637839607}')
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('y123456')
        log.info(f'输入的密码是：{"y123456"}')
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(2)
        a= self.dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[-1].text
        #self.assertEqual(a, '我的', msg="断言登录成功")
        log.info('登录成功的处理')
    def test_1(self):
        self.dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[1].click()
        sleep(2)
        log.info('点击消息，进入消息界面')
        try:
            log.info('进入失败的处理')
            b = self.dr.find_elements_by_id('com.qk.butterfly:id/v_search')[0].text
            self.assertEqual(b, '蝶声交友', msg='断言进入失败')

        except:
            log.info('进入成功消息的处理')
            a = self.dr.find_element_by_id('com.qk.butterfly:id/tv_message_title').text
            self.assertEqual(a, '我的消息', msg='断言已经进入成功')
    def test_2(self):
        log.info('点击排行，进入排行界面')
        self.dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[2].click()
        sleep(2)
        try:
            log.info('进入失败的处理')
            b = self.dr.find_elements_by_id('com.qk.butterfly:id/v_search')[0].text
            self.assertEqual(b, '蝶声交友', msg='断言进入失败')
        except:
            a = self.dr.find_element_by_id('com.qk.butterfly:id/tv_title').text
            self.assertEqual(a, '排行榜', msg='断言已经进入成功')
            log.info('进入成功排行的处理')
            print('进入成功')
    def test_3(self):
        log.info('点击我的，进入我的界面')
        self.dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[-1].click()
        try:
            log.info('进入失败我的处理')
            b=self.dr.find_element_by_id('com.qk.butterfly:id/framelayout').find_elements_by_class_name('android.widget.TextView')[0].text
            self.assertEqual(b, '蝶声交友', msg='断言进入失败')
        except:
            a=self.dr.find_element_by_id('com.qk.butterfly:id/framelayout').find_elements_by_class_name('android.widget.TextView')[0].text
            self.assertEqual(a, '我的', msg='断言已经进入成功')
            log.info('成功进入我的处理')
    def test_4(self):
        log.info('点击我的，进入我的界面')
        sleep(2)
        self.dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[-1].click()
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
        sleep(2)
        self.dr.find_elements_by_id('com.qk.butterfly:id/v_me_grade')[-1].click()
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
        sleep(2)
        try:
            log.info('退出失败的处理')
            a = self.dr.find_elements_by_id('com.qk.butterfly:id/v_me_gold')[1].text
            self.assertEqual(a, '金币充值', msg='断言退出失败')

        except:
            log.info('退出成功的处理')
            b = self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').text
            self.assertEqual(b, '登录', msg='断言退出成功')

            sleep(2)
    @classmethod
    def tearDownClass(self):
        log.info('手机与appium断开连接')
        self.dr.quit()

if __name__ == '__main__':
    # unittest.main()
    baogao.csbg((TC('test_1'),TC('test_2'),TC('test_3'),TC('test_4')), report_path=r'F:\学习总结\python\untitled6\Tim\diesheng\report\a.html')