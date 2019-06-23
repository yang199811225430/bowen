#！/user/bin/python
#-*- coding:utf-8 -*-

import requests
from data.duqu import *

class KD_x(object):
    def cha_ming(self,num):
        url="https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/deliveryInfo"
        header={     'Content-Type': "application/json",
                    'x-dealer-code': "2100001",
                    'x-position-code': "D_PO_1028",
                    'x-resource-code': "pol4s_partOrderSearch_deliveryInfo",
                    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                    'x-user-code': "dhxc1u",
                    'x-access-token': "8405e48dd499a8a329afe8e8d8e7da3b",
                    'User-Agent': "PostmanRuntime/7.15.0",
                    'Accept': "*/*",
                    'Cache-Control': "no-cache",
                    'Postman-Token': "a32bd0ab-084b-46d9-b5a0-e99c7b840fde,ad710f79-364a-4b54-b0c7-f092d301525a",
                    'Host': "mobileqa.dms.saic-gm.com",
                    'cookie': "dapp.sgm.com:qa:=8405e48dd499a8a329afe8e8d8e7da3b; dapp.sgm.com:qa:=8405e48dd499a8a329afe8e8d8e7da3b; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=a3a54f569b14d5196ef24d5b4b890058",
                    'accept-encoding': "gzip, deflate",
                    'content-length': "82",
                    'Connection': "keep-alive",
                    'cache-control': "no-cache"
                                                }

        py="{\r\n\"pageSize\":10,\r\n\"pageNum\":1,\r\n\"queryTerms\":\r\n{ \"orderNo\":\"\",\r\n\"partNo\":\"\"\r\n}\r\n}"
        res=requests.post(url=url,headers=header,data=py)
        return res.json()
if __name__=="__main__":
    for i in shuju():
        a=KD_x().cha_ming(i[0])
        print(a)