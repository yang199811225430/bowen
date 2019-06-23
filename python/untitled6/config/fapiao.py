#！/user/bin/python
#-*- coding:utf-8 -*-

import requests
from data.duqu import *

class Fa_piao(object):
    def cha_ming(self,num):
        url="https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderElectricInvoice"
        header={   'Content-Type': "application/json",
                    'x-dealer-code': "2100001",
                    'x-position-code': "D_PO_1028",
                    'x-resource-code': "pol4s_partOrder_orderElectricInvoice",
                    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                    'x-user-code': "dhxc1u",
                    'x-access-token': "c909d3541a63a46b75f314a4e94828c0",
                    'cache-control': "no-cache",
                    'Postman-Token': "44c29941-fd40-47d4-912f-310bae0b4aec"}
        py="{\r\n \"orderNo\": \"R2100005181116190\"\r\n}"
        res=requests.post(url=url,headers=header,data=py)
        return res.json()
if __name__=="__main__":
    for i in shuju():
        a=Fa_piao().cha_ming(i[1])
        print(a)
