#！/user/bin/python
#-*- coding:utf-8 -*-
from config.fapiao import *
from data.duqu import *
import unittest
class ding(unittest.TestCase):
    ss=shuju()
    def test_1(self):
        b=Fa_piao().cha_ming(self.ss[0][0])
        self.assertEqual(b['errMsg'],'处理成功')
    def test_2(self):
        aa=Fa_piao().cha_ming(self.ss[1][0])
        self.assertNotIn( "处理失败",aa)
    def test_3(self):
        aa=Fa_piao().cha_ming(self.ss[2][0])
        self.assertNotIn('null',aa)
    def test_4(self):
        aa=Fa_piao().cha_ming(self.ss[3][0])
        self.assertEqual(aa['data']['orderNo'],'R2100005181213490')
if __name__=="__main__":
     unittest.main()