#！/user/bin/python
#-*- coding:utf-8 -*-

import requests
from data.duqu import *

class Pei_j(object):
    def cha_ming(self,num):
        url="https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail"
        header={  'Content-Type': "application/json",
                    'x-dealer-code': "2100001",
                    'x-position-code': "D_PO_1028",
                    'x-resource-code': "pol4s_partOrder_orderPartDetail",
                    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                    'x-user-code': "dhxc1u",
                    'x-access-token': "8405e48dd499a8a329afe8e8d8e7da3b",
                    'User-Agent': "PostmanRuntime/7.15.0",
                    'Accept': "*/*",
                    'Cache-Control': "no-cache",
                    'Postman-Token': "232cfad2-e219-4899-9cd0-e5827b90c118,06eac906-8843-4a47-bb7f-876c97deb8f8",
                    'Host': "mobileqa.dms.saic-gm.com",
                    'cookie': "dapp.sgm.com:qa:=8b9b4159924fe441e96e533a4ddf3f32; dapp.sgm.com:qa:=8b9b4159924fe441e96e533a4ddf3f32; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
                    'accept-encoding': "gzip, deflate",
                    'content-length': "30",
                    'Connection': "keep-alive",
                    'cache-control': "no-cache"
                            }
        py="{\r\n \"partOrderItemId\": 3108\r\n}"
        res=requests.post(url=url,headers=header,data=py)
        return res.json()
if __name__=="__main__":
    for i in shuju():
        a=Pei_j().cha_ming(i[0])
        print(a)
