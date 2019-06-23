#!/usr/bin/python
#-*- coding:utf-8 -*-
#不用int将字符串变为整数
# a='123'
# c=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             c+=j*10**(len(a)-1-i)
# print(type(c))


#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     if i==j:
#         print()


#创建一个目录aaa在aaa下创建一个a.txt，给a.txt写入多行数据，删除a.txt，删除aaa
# import os
# os.mkdir('aaa')
# f=open(r'F:\学习总结\python\untitled1\a.txt','w+',encoding='utf-8')
# while True:
#     a=input('>>>')
#     if a!='exit':
#         f.write(a+'\n')
#     else:
#         f.close()
#         break
# os.remove(r'F:\学习总结\python\untitled1\a.txt')
# os.rmdir('aaa')


#将a.txt导入到数据库中
# import pymysql
# with open('a.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# noon=pymysql.connect(host='192.168.0.222',port=3306,user='root',passwd='112233')
# m=noon.cursor()
# m.execute('use test')
# for i in range(len(a)):
#     c=a[i].split(',')
#     if i==0:
#          m.execute('create table a({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0], c[1], c[2], c[3]))
#     else:
#          m.execute('insert into uuu values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
# m.execute('select * from uuu ')
# d=m.fetchall()
# print(d)
# noon.close()



# #socket 通信
# # #S:
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.73',3000))
# s.listen(3)
# while True:
#     client,addr=s.accept()
#     reg=client.recv(1024)
#     print(reg.decode('utf-8'))
#     msg=input('>>>')
#     client.send(msg.encode('utf-8'))


# # #C:
# # import socket
# # sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # sock.connect(('192.168.0.73',3000))
# # while True:
# #     qq=input('>>>')
# #     if qq=='关闭':
# #         sock.close()
# #     else:
# #         sock.send(qq.encode('utf-8'))
# #         ww=sock.recv(1024)
# #         print(ww.decode('utf-8'))

# #发邮件
# import smtplib
# import email.mime.multipart as mu
# import email.mime.text as text
# mm='17637839607@163.com'
# yy='18317822978@163.com'
# message=mu.MIMEMultipart()
# message['Subject']='python_test'
# message['From']=mm
# message['To']=yy
# txt="""
# 你好！
# """
# tet=text.MIMEText(txt)
# message.attach(tet)
# att1=text.MIMEText(open('b.xls', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="b.xls"'
# message.attach(att1)
# smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login(mm,'yang1998')
# smtp123.sendmail(mm,yy,message.as_string())

# import re
# import requests
# # class FreeBuf():
# #     def send_qq(self,page):
# #         url='https://www.freebuf.com/page/{}'.format(page)
# #
# #         res=requests.post(url)
# #         hh=res.content.decode('utf-8')
# #         return hh
# #     def gl(self,x):
# #         title=[]
# #         patt=re.compile('<div class="news-img">(.*?)<dd>',re.S)
# #         itesms=patt.findall(x)
# #         for i in itesms:
# #             aa=re.findall('title="(.*?)"',i)
# #             title.append(aa[0])
# #         return title
# #     def save(self,y):
# #         with open('a.txt','a',encoding='utf-8') as f:
# #             for i in y:
# #                 f.write(i+'\n')
# # fr=FreeBuf()
# # for i in range(1,5):
# #     hh=fr.send_qq(i)
# #     gg=fr.gl(hh)
# #     fr.save(gg)
#
#
# import re
# import requests
# import json
# import pymysql
# conn = pymysql.connect(host='192.168.0.222', port=3306, user='root', passwd='112233')
# m = conn.cursor()
# m.execute('use test')
# m.execute('create table zhilian(公司 char(45),工作经验 char(35),薪资 char(15),公司地点 char(10),学历 char(10))')
# class FreeBuf():
#     def send_qq(self):
#         url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.74126408&x-zp-page-request-id=b429b90a62204889bf7614c344f186e2-1557230138170-687758'
#         head = {
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#             }
#         res=requests.get(url,headers=head)
#         hh=res.content.decode('utf-8')
#         bb=json.loads(hh)
#         return bb
#     def gl(self,x):
#         aa=len(x['data']['results'])
#
#         for i in range(aa):
#             c = []
#             c.append(x['data']['results'][i]['company']['name'])
#             c.append(x['data']['results'][i]['workingExp']['name'])
#             c.append(x['data']['results'][i]['salary'])
#             c.append(x['data']['results'][i]['city']['display'])
#             c.append(x['data']['results'][i]['eduLevel']['name'])
#             m.execute('insert into zhilian values("{}","{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3],c[4]))
# fr=FreeBuf()
# hh=fr.send_qq()
# gg=fr.gl(hh)





