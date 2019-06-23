#！/user/bin/python
#-*- coding:utf-8 -*-
from config.peijian import *
from data.duqu import *
import unittest
class ding(unittest.TestCase):
    ss=shuju()
    def test_1(self):
        b=Pei_j().cha_ming(self.ss[0][0])
        self.assertEqual(b['errMsg'],'处理成功')
    def test_2(self):
        aa=Pei_j().cha_ming(self.ss[1][0])
        self.assertNotIn( "处理失败",aa)
    def test_3(self):
        aa=Pei_j().cha_ming(self.ss[2][0])
        self.assertNotIn('null',aa)
    def test_4(self):
        aa=Pei_j().cha_ming(self.ss[3][0])
        self.assertEqual(aa['status'],1)
if __name__=="__main__":
     unittest.main()