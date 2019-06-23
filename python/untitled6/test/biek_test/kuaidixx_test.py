#！/user/bin/python
#-*- coding:utf-8 -*-
from config.kuaidi import *
from data.duqu import *
import unittest
class ding(unittest.TestCase):
    ss=shuju()
    def test_1(self):
        b=KD_x().cha_ming(self.ss[0][0])
        self.assertEqual(b['errMsg'],'订单或配件信息为空！')
    def test_2(self):
        aa=KD_x().cha_ming(self.ss[1][0])
        self.assertNotIn( "处理失败",aa)
    def test_3(self):
        aa=KD_x().cha_ming(self.ss[2][0])
        self.assertNotIn('null',aa)
    def test_4(self):
        aa=KD_x().cha_ming(self.ss[3][0])
        self.assertEqual(aa['status'],0)
if __name__=="__main__":
     unittest.main()

