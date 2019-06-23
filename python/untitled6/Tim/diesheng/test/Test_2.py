from Tim.diesheng.test.Test_1 import *
des = {"platformName": "Android",
                       "platformVersion": "5.1.1",
                       "deviceName": "emulator-5554",
                       "appPackage": "com.qk.butterfly",
                       "appActivity": ".main.LauncherActivity",
                       "unicodeKeyboard": "True",
                       "resetKeyboard": "True",
                       "noReset": "true"
                }
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
sleep(2)
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
sleep(2)
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(17637839607)
sleep(2)
dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('y123456')
sleep(2)
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
sleep(5)
dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[-1].click()
sleep(2)
a=dr.find_elements_by_id('com.qk.butterfly:id/v_me_gold')[1].text
print(a)