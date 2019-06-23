#！/user/bin/python
#-*- coding:utf-8 -*-
from config.dingdan import *
from data.duqu import *
import unittest
class ding(unittest.TestCase):
    ss=shuju()
    def test_1(self):
        b=Dingdan_1().cha_ming(self.ss[0][0])
        self.assertEqual(b['errMsg'],None)
    def test_2(self):
        aa=Dingdan_1().cha_ming(self.ss[1][0])
        self.assertNotIn( "处理成功",aa)
    def test_3(self):
        aa=Dingdan_1().cha_ming(self.ss[2][0])
        self.assertEqual(aa['status'],1)
    def test_4(self):
        aa=Dingdan_1().cha_ming(self.ss[3][0])
        self.assertNotIn('V2100880181219391',aa)
if __name__=="__main__":
     unittest.main()