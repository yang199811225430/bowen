#！/user/bin/python
#-*- coding:utf-8 -*-

import requests
from data.duqu import *

class Dingdan_1(object):
    def cha_ming(self,num):
        url="https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch"
        header={    'Content-Type': "application/json",
                    'x-dealer-code': "2100001",
                    'x-position-code': "D_PO_1028",
                    'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
                    'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                    'x-user-code': "dhxc1u",
                    'x-access-token': "c909d3541a63a46b75f314a4e94828c0",
                    'cache-control': "no-cache",
                    'Postman-Token': "1701fb41-b6cf-4823-8542-98765d3fcf9c"}
        py="{\n\t\"pageNum\":\"%d\",\n\t\"pgeSize\":\"10\",\n\t\"queryTerms\":\n\t{\n\t\t\"orderNo\":\"V2100880181219390\"\n\t}\n}" %(num)
        res=requests.post(url=url,headers=header,data=py)
        return res.json()
if __name__=="__main__":
    for i in shuju():
        a=Dingdan_1().cha_ming(i[0])             
        print(a)
