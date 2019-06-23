# #!/usr/bin/python
# #-*- coding:utf-8 -*-
# a=int(input('请输入总资产'))
# c=''
# goods=[
#     {'0':'电脑','prince':1999},
#     {'1':'鼠标','prince':10},
#     {'2':'游艇','prince':20},
#     {'3':'美女','prince':998},
# ]
# class Mdx():
#     def __init__(self,a):
#         self.a=a
#     def gwc(self,*x):
#         c=[]
#         for i in range(len(x)):
#             if len(goods) >= x[i]:
#                 b=x[i]
#                 v=goods[b]
#                 c.append(v)
#         return c
#     def gm(self,x):
#         g=0
#         for i in x:
#             w=i['prince']
#             g+=w
#         if  self.a>=g:
#             self.a-=g
#             print('购买成功，余额为{}元'.format(self.a))
#         else:
#             print('余额不足请充值')
#     def cz(self,q):
#         self.a = q + self.a
#         print('充值成功，余额{}元'.format(self.a))
#     def yc(self,x,*y):
#         for i in y:
#             print(x)
#             s=x
#             s.pop(y)
#         print(s)
#
# m=Mdx(a)
# hh=m.gwc(1,2)
# m.gm(hh)


# print(goods)
# p = len(goods)
# while True:
#     try:
#         q = int(input('序号'))
#         if  p >= q:
#             c=list(c)
#             v=goods[q]
#             print(v)
#             c.append(v)
#             print(c)
#         elif p<q:
#             print('该商品不存在')
#     except:
#         break
# print(c)
# b=len(c)
# while True:
#     q=input('')
#     g=0
#     if q=='移除商品':
#         print(c)
#         e=int(input(''))
#         c.pop(e)
#         print(c)
#     elif q=='购买':
#         for i in c:
#             w=i['prince']
#             g+=w
#         print(g)
#         while True:
#             if a>=g:
#                 a = a - g
#                 print('购买成功，余额{}元'.format(a))
#                 break
#             if a<g and a!=0:
#                 print('余额不足，请充值')
#                 if input()=='充值':
#                     y=int(input(''))
#                     a=y+a
#                     print('充值成功，余额{}元'.format(a))
#         break









# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.98',3000))
# s.listen(3)
# while True:
#     client,addr=s.accept()
#     reg=client.recv(1024)


#     print(reg.decode('utf-8'))
#     msg=input('>>>')
##     client.send(msg.encode('utf-8'))

# import socket
# # s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # host=(('192.168.0.88',3000))
# # while True:
# #     qq=input('>>>')
# #     s.sendto(qq.encode('utf-8'),host)
# #     ww=s.recv(1024)
# #     print(ww.decode('utf-8'))

# class Asd():
#     def __init__(self,x,y):
#         self.name=x
#         self.xueliang=y
#     def ad(self):
#         self.xueliang -= 100
#         print('{}还有{}血'.format(self.name,self.xueliang))
#     def ert(self):
#         # self.xueliang += 200
#         # print('{}还有{}血'.format(self.name,self.xueliang))
# q=Asd('一航',200)
# p=Asd('幺妹',300)
# q.ad()
# p.ert()





# """
# 电话键
#
# KEYCODE_CALL 拨号键 5
# KEYCODE_ENDCALL 挂机键 6
# KEYCODE_HOME 按键Home 3
# KEYCODE_MENU 菜单键 82
# KEYCODE_BACK 返回键 4
# KEYCODE_SEARCH 搜索键 84
# KEYCODE_CAMERA 拍照键 27
# KEYCODE_FOCUS 拍照对焦键 80
# KEYCODE_POWER 电源键 26
# KEYCODE_NOTIFICATION 通知键 83
# KEYCODE_MUTE 话筒静音键 91
# KEYCODE_VOLUME_MUTE 扬声器静音键 164
# KEYCODE_VOLUME_UP 音量增加键 24
# KEYCODE_VOLUME_DOWN 音量减小键 25
#
# 控制键
#
# KEYCODE_ENTER 回车键 66
# KEYCODE_ESCAPE ESC键 111
# KEYCODE_DPAD_CENTER 导航键 确定键 23
# KEYCODE_DPAD_UP 导航键 向上 19
# KEYCODE_DPAD_DOWN 导航键 向下 20
# KEYCODE_DPAD_LEFT 导航键 向左 21
# KEYCODE_DPAD_RIGHT 导航键 向右 22
# KEYCODE_MOVE_HOME 光标移动到开始键 122
# KEYCODE_MOVE_END 光标移动到末尾键 123
# KEYCODE_PAGE_UP 向上翻页键 92
# KEYCODE_PAGE_DOWN 向下翻页键 93
# KEYCODE_DEL 退格键 67
# KEYCODE_FORWARD_DEL 删除键 112
# KEYCODE_INSERT 插入键 124
# KEYCODE_TAB Tab键 61
# KEYCODE_NUM_LOCK 小键盘锁 143
# KEYCODE_CAPS_LOCK 大写锁定键 115
# KEYCODE_BREAK Break/Pause键 121
# KEYCODE_SCROLL_LOCK 滚动锁定键 116
# KEYCODE_ZOOM_IN 放大键 168
# KEYCODE_ZOOM_OUT 缩小键 169
#
# 组合键
#
# KEYCODE_ALT_LEFT Alt+Left
# KEYCODE_ALT_RIGHT Alt+Right
# KEYCODE_CTRL_LEFT Control+Left
# KEYCODE_CTRL_RIGHT Control+Right
# KEYCODE_SHIFT_LEFT Shift+Left
# KEYCODE_SHIFT_RIGHT Shift+Right
#
# 基本
#
# KEYCODE_0 按键'0' 7
# KEYCODE_1 按键'1' 8
# KEYCODE_2 按键'2' 9
# KEYCODE_3 按键'3' 10
# KEYCODE_4 按键'4' 11
# KEYCODE_5 按键'5' 12
# KEYCODE_6 按键'6' 13
# KEYCODE_7 按键'7' 14
# KEYCODE_8 按键'8' 15
# KEYCODE_9 按键'9' 16
# KEYCODE_A 按键'A' 29
# KEYCODE_B 按键'B' 30
# KEYCODE_C 按键'C' 31
# KEYCODE_D 按键'D' 32
# KEYCODE_E 按键'E' 33
# KEYCODE_F 按键'F' 34
# KEYCODE_G 按键'G' 35
# KEYCODE_H 按键'H' 36
# KEYCODE_I 按键'I' 37
# KEYCODE_J 按键'J' 38
# KEYCODE_K 按键'K' 39
# KEYCODE_L 按键'L' 40
# KEYCODE_M 按键'M' 41
# KEYCODE_N 按键'N' 42
# KEYCODE_O 按键'O' 43
# KEYCODE_P 按键'P' 44
# KEYCODE_Q 按键'Q' 45
# KEYCODE_R 按键'R' 46
# KEYCODE_S 按键'S' 47
# KEYCODE_T 按键'T' 48
# KEYCODE_U 按键'U' 49
# KEYCODE_V 按键'V' 50
# KEYCODE_W 按键'W' 51
# KEYCODE_X 按键'X' 52
# KEYCODE_Y 按键'Y' 53
# KEYCODE_Z 按键'Z' 54
# """


#建立与appuim服务器的参数，以字典的形式
from time import *
from appium import webdriver
# des={"platformName": "Android",
#      "platformVersion": "5.1.1",
#      "deviceName": "emulator-5554",
#      "appPackage": "com.tencent.tim",
#      "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#      "unicodeKeyboard":"True",
#      "resetKeyboard":"True",
#
#      "noReset": "true"
#      }


# des={"platformName": "Android",
#      "platformVersion": "5.1.1",
#      "deviceName": "emulator-5554",
#      "appPackage": "com.ss.android.ugc.aweme",
#      "appActivity": ".main.MainActivity",
#      "unicodeKeyboard":"True",
#      "resetKeyboard":"True",
#      "noReset": "true"
#      }




#http://127.0.0.1:4723/wd/hub  固定的，localhost=127.0.0.1
#测试脚本与appuim服务器建立一个session连接
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
# sleep(5)
#层级定位
#第一步，先定义一个唯一的元素
#第二步，再定义多个相同的元素
# items=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# #print(items)
# for i in items:
#   sleep(0.5)
#   i.click()
#   sleep




# dr.find_element_by_class_name('android.widget.Button').click()
# sleep(2)
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').clear()
# sleep(2)
# dr.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱").send_keys('1508295989')
# sleep(2)
# dr.find_element_by_id('com.tencent.tim:id/password').send_keys('y1onlyloveyou')
# sleep(2)
# dr.find_element_by_id('com.tencent.tim:id/login').click()
# sleep(2)
#关闭
#dr.quit()
#第一步，获取手机屏幕大小
# s=dr.get_window_size()
# #第二步放缩x、y轴
# x1=s['width']*0.5
# y1=s['height']*0.5
# y2=s['width']*0.25
# #第三步 使用swipe方法，进行滑动操作
# dr.swipe(x1,y1,x1,y2)






# a=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# sleep(2)
# a[2].click()
# sleep(5)
# b=dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name('android.widget.RelativeLayout')
# sleep(2)
# b[6].click()
# sleep(10)
# s=dr.get_window_size()
# x1=s['width']*0.5
# y1=s['height']*0.5
# y2=s['height']*0.25
# dr.swipe(x1,y1,x1,y2)
# sleep(2)
# c=dr.find_elements_by_class_name('android.widget.ImageView')
# sleep(2)
# c[1].click()

# 关闭
# dr.quit()




# #面向对象
# class Tim(object):
#     def __init__(self):
#         self.des = {"platformName": "Android",
#                "platformVersion": "5.1.1",
#                "deviceName": "emulator-5554",
#                "appPackage": "com.tencent.tim",
#                "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#                "unicodeKeyboard": "True",
#                "resetKeyboard": "True",
#
#                "noReset": "true"
#                }
#         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
#         sleep(5)
#     def dz(self):
#         a= self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
#         sleep(2)
#         a[2].click()
#         sleep(5)
#         b=self.dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name('android.widget.RelativeLayout')
#         sleep(2)
#         b[6].click()
#         sleep(10)
#         # s=self.dr.get_window_size()
#         # x1=s['width']*0.5
#         # y1=s['height']*0.5
#         # y2=s['height']*0.25
#         # self.dr.swipe(x1,y1,x1,y2)
#         # sleep(2)
#         # c=self.dr.find_elements_by_class_name('android.widget.ImageView')
#         # sleep(2)
#         # c[1].click()
#
#
# #获取文字
#     def g(self):
#         a= self.dr.find_element_by_id('com.tencent.tim:id/ivTitleName').text
#         print(a)
#         return a
#     def aj(self):
#         #模拟人点击物理按键
#         #点击home键
#         #self.dr.keyevent(3)
#         #点击返回键
#         #self.dr.keyevent(4)
#         #点击相机开启
#         self.dr.keyevent(27)
# if __name__ == '__main__':
#     k= Tim()
#     k.aj()





# #面向对象
class   DY(object):
    def __init__(self):
        self.des = {"platformName": "Android",
               "platformVersion": "5.1.1",
               "deviceName": "emulator-5554",
               "appPackage": "com.ss.android.ugc.aweme",
               "appActivity": ".main.MainActivity",
               "unicodeKeyboard": "True",
               "resetKeyboard": "True",

               "noReset": "true"
               }
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5)
    def dz(self):
        a= self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
        sleep(2)
        a[2].click()
        sleep(5)
        b=self.dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name('android.widget.RelativeLayout')
        sleep(2)
        b[6].click()
        sleep(10)
        # s=self.dr.get_window_size()
        # x1=s['width']*0.5
        # y1=s['height']*0.5
        # y2=s['height']*0.25
        # self.dr.swipe(x1,y1,x1,y2)
        # sleep(2)
        # c=self.dr.find_elements_by_class_name('android.widget.ImageView')
        # sleep(2)
#         # c[1].click()
    def hua(self):
        s = self.dr.get_window_size()
        x1=s['width']*0.5
        y1=s['height']*0.5
        y2=s['height']*0.25
        while True:
            self.dr.swipe(x1,y1,x1,y2)
            sleep(15)
if __name__=='__main__':
    d=DY()
    d.hua()