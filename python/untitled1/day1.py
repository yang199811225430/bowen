#!/usr/bin/python  #定义一个解释器
#-*- coding:utf-8 -*-  定义编码方式
#print('hello',123,456,789)   输出
# a=input('请输入密码:')
#print(a)
#a,b,c='ycx',1,2.1
#print(b+c)
#print(type(c))
# a='asbf1234de'
# print(a[2::-2])
#b=a.upper()
#b=a.replace(' ','',3)
#b=a.split('bf')
#b=a.rstrip()
#b=a.startswith('asb')
#b=a.endswith('de')
#c='+'.join(b)
#a='{a1},{a2},{a3},{a4}'
#c=a.format(a1='我',a2='爱',a3='我',a4='家')
#a='hello %s，我今年%d岁'
#b=a% ('小明',1000000)
#a='qewwre'
#b=a.index('w')
#a='qwewwrt'
#b=a.count('w')
#a=[1,'我',2,9,6]
#a.insert(4,5)
#print(a)
# a=0
# for i in range(2,101,1):
#     for j in range(2,i+1,1):
#         if i % j ==0:
#            #print(i)
#            break
#     if i == j:
#         a=a+i
# print(a)
# a=input('请输入字符串')
# b=len(a)
# q=a[i]
# w=a[-(i+1)]
# c=b//2
# #if a ==a[::-1]:
#     #print('这是一个回文字符串')
# #else:
#     #print('这不是一个回文字符串')
#     #if b %2==0:
# for i in range(c):
#     if q !=w:
#         print('这不是一个回文字符串')
#         break
#     else:
#         print('这是一个回文字符串')
# a=1
# b=0
# while a<101:
#     b+=a
#     a+=1
# print(b)
# while True:
#     a=input("输入成绩")
#     a=a.split(',')
#     a=[int(i) for i in a]
#     d=sum(a)//len(a)
#     if a[0]< 0:
#         break
#     print('平均数为{}'.format(d))
#     b = [k for k in a if k < d]
#     print(b)

# a=[1,5,6,8,7,8,9,5,7]
# for k in a:
#     if a[k] == a[k+1]:
#         a.remove(a[k])
#     else:
#         break
#     print(a)
# a=[1,5,6,8,7,8,9,5,7]
# for i in a:
#     b=a.count(i)
#     if b>1:
#         for j in range(b-1):
#             a.remove(i)
#             b=a.sort()
# print(a)
# a=[1,5,6,8,7,8,9,5,7]
# b=[]
# for i in a:
#     if a not in b:
#         b.append(a)
#     print(b)
# f=open(r'a.txt','w',encoding='utf-8')
# f.write('sadf')
# f.close()
# f=open(r'a.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         f.write('{}*{}={}\t'.format(i,j,i*j))
#     f.write('\n')
# f.close()
# f=open(r'a.txt','r',encoding='utf-8')
# b=f.readlines()
# #print(b)
# for i in b:
#      if print(i.startswith('abc'))==True:
#         print(i)
#
#
# f.close()
# f=open(r'a.txt','r',encoding='utf-8')
# b=f.readlines()
# #print(b)
# for i in b:
#      if i[:3]=='abc':
#         print(i)
#
#
# f.close()
# f=open(r'a.txt','r',encoding='utf-8')
# b=f.readlines()
# print(b[14],b[15],b[16],b[17],b[18],b[19])
# f.close()
# f=open(r'a.txt','r',encoding='utf-8')
# for i in range(1,21):
#     if i<15:
#         f.readline()
#     else:
#         print(f.readline())
# f.close()
# import random
# a=random.randrange(1,10)
# print(a)
# for i in  range(1,4):
#     b=input('请输入数字')
#     b=int(b)
#     if b==a:
#         print('恭喜你答对了')
#         break
#     elif i==3:
#         print('真菜')
#     elif b>a:
#         print('大了大了还有{}次机会'.format(3-i))
#     elif b<a:
#        print('小了小了还有{}次机会'.format(3-i))
# a=input('请输入')
# a=a.split(',')
# a=[int(i) for i in a]
# for i in  range(1,len(a)):
#     for j in range(0,len(a)-1):
#         if a[j]>a[j+1]:
#             t=a[j]
#             a[j] = a[j+1]
#             a[j+1]=t
# print(a)
# a=input('请输入')
# a=a.split(',')
# a=[int(i) for i in a]
# for b in range(0,len(a)):
#     for j in  range(b+1,len(a)):
#         if a[b] > a[j]:
#             t=a[b]
#             a[b]=a[j]
#             a[j]=t
# print(a)
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if i==a**3+b**3+c**3:
#         print(i)
# a=1
# b=0
# for i in  range(1,101):
#     a=i*a
#     b=a+b
# print(b)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     if i==j:
#         print()
# for i in range(50):
#     for j in range(100):
#         b=100-i-j
#         if i*2+j*1+b*0.5==100 :
#             print(i,j,b)
# with open('a.txt','r+',encoding='utf-8') as  f:
# #     b=f.read()
# #     f.write('河山')
# # print(b)
# def a():
#     b=0
#     for i in  range(101):
#         b+=i
#     print(b)
# a='123'
# c=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             c+=j*10**(len(a)-1-i)
# print(c)
# a=[1,9,9,8,7,9,8,5,6]
# b=a.reverse()
# print(a)
# b=1
# def a():
#     global b    #将局部变量变为全局变量
#     b=0
#     print(b)
# a()
# print(b)
# def a(b):
#     print('hello')
#     print(b)
# a(1)
# def a(b=100):
#     x=0
#     for i in range(b+1):
#         x+=i
#     print(x)
# a()
# def zs(q,w):
#     a=0
#     for i in range(q,w+1):
#         for j in range(2,i+1):
#             if i % j ==0:
#                 break
#         if i == j:
#             a=a+i
#     print(a)
# zs(2,10)
# def a(c):
#      x=0
#      for i in range(1,c+1):
#           x+=i
#      return x
# for i in range(10,41,10):
#      c=a(i)+2
#      print(c)
# def jsq(x,y,z):
#     q=0
#     if y=='+':
#         q=x+z
#     elif y=='-':
#         q=x-z
#     elif y=='*':
#         q=x*z
#     elif y=='//':
#         q=x//z
#     elif y=='/':
#         q=x/z
#     return q
# print(jsq(6,'-',2))
# a =lambda x,y :x + y
# b =lambda x,y :x - y
# c =lambda x,y :x * y
# d =lambda x,y :x / y
# while True:
#     s=input('请输入')
#     if '-' in s:
#         q=s.split('-')
#         print(b(int(q[0]),int(q[1])))
#     elif '+' in s:
#         q= s.split('+')
#         print(a(int(q[0]),(q[1])))
#     elif '*' in s:
#         q = s.split('*')
#         print(c(int(q[0]),(q[1])))
#     elif '/' in s:
#         q = s.split('/')
#         print(d(int(q[0]),(q[1])))
#     else:
#         break
# def sc(a,b,c):
#     a=list(a)
#     z=len(a)
#     if z-b<b+c:
#vgv
#
#
#     elif z-b>b+c:
#         for i in range(b,b+c):
#
#             b='',join(a)
#     print(b)
# sc('qwert',1,3)
# a=input('请输入')
# ff=[str(i) for i in  range(10)]+['a','b','c','d','e','f']
# c=''
# while True:
#     a=int(a)
#     b=a%16
#     c=c+ff[b]
#     a=a//16
#     if a==0:
#         break
# print(c[::-1])
# a=input('请输入')
# b=a.split(',')
# b=[int(i) for i in b]
# b.sort()
# c=[]
# d=b.count(b[-1])
# for j in range(1,d+1):
#     c.append(b[-1])
#     b.remove(b[-1])
# f=b.count(b[-1])
# for j in range(1,f+1):
#     c.append(b[-1])
# print(c)
# def asd():
#     print('hello')
# def qwe():
#     print(123)
# if __name__=='__main__':
#     for i in  range(10):
#         print(i)
# try:
#     a=1
#     print(a)
# except Exception as e:
#     print(e)
# else:
#     print(789)
# finally:
#     print(456)

#将九九乘法表写入a.xls
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('python_test')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))
# f.save('a.xls')

#读取excel表的第15到20行的内容
# import xlrd
# f=xlrd.open_workbook('a.xls')
# # b=f.nsheets
# # sheet=f.sheets()[0]
# #b=f.sheet_names()
# sheet=f.sheet_by_name('python_test')
# b=sheet.ncols
# for i in range(15,21):
#     c=sheet.row_values(i)
#     print(c)
# b=sheet.cell(2,0).value
# print(b)


#将文件里的内容写入到excel表格中
# import  xlwt
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('python_test')
# c=[]
# f=open('a.txt','r',encoding='utf-8')
# b=f.readlines()
# for i in range(len(b)):
#     q=b[i]
#     w=q.split(',')
#     c.append(w)
#     u=c[0]
# f.close()
# for j in range(len(b)):
#     for z in range(len(u)):
#         sheet.write(j,z,c[j][z])
# ff.save('a.xls')





#将b.txt追加到excel表中
# from xlutils.copy import copy
# import xlrd
# c=[]
# f=xlrd.open_workbook('a.xls')
# sheet1=f.sheet_by_name('python_test')
# b=sheet1.ncols
# a=sheet1.nrows
# print(b,a)
# ff=open('b.txt','r',encoding='utf-8')
# bb=ff.readlines()
# for i in range(len(bb)):
#     q=bb[i]
#     w=q.split(',')
#     c.append(w)
#     print(c)
#     u=c[0]
#     #print(len(b))
# ff.close()
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# for i in range(len(bb)):
#     for j in range(len(u)):
#         sheet.write(i+a,j,c[i][j])
# new_f.save('a.xls')





# import time
# b=time.localtime(100)
# a=time.strptime('2011-10-01 12:25:00','%Y-%m-%d %H:%M:%S')
# time.sleep(0)
# b=(2019,4,18,11,24,0,456,789,1)
# a=time.mktime(b)
# print(a)


#输入一个日期 显示是否为闰年 一年中的第几天  星期几  前一天
# import time
# a=input('')
# b=time.strptime(a,'%Y-%m-%d')
# print(b)
# if b[0]%100==0:
#     if b[0]%400==0:
#         print('{}年为闰年'.format(b[0]))
#     else:
#         print('{}年不是闰年'.format(b[0]))
# else:
#     if b[0]%4==0:
#         print('{}年为闰年'.format(b[0]))
#     else:
#         print('{}年不是闰年'.format(b[0]))
# print('一年中的第{}天'.format(b[7]))
#
# print('今天星期{}'.format(b[6]+1))
# c=(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8])
# a=time.localtime(time.mktime(c)-86400)
# print('前一天为{}年{}月{}日'.format(a[0],a[1],a[2]))




#将a.xls文件中的数据写入b.txt中
# import xlrd
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[1]
# b=sheet.nrows
# print(b)
# ff=open('b.txt','w+',encoding='utf-8')
# for i in range(b):
#     c=sheet.row_values(i)
#     c=' '.join(c)
#     ff.write('{}'.format(c))
#     ff.write('\n')
# ff.close()



#求和、平均数 并把小于平均数的打印出来
# def a(*c):
#     b=0
#     for i in  range(len(c)):
#         b=c[i]+b
#     print(b)
#     e=b/len(c)
#     print(e)
#     for j in range(len(c)):
#         if c[j]<e and c[j]>0:
#             print(c[j])
#         elif c[j]<0:
#             break
# a(6,1,-1)
#



#对数据库的操作
# import pymysql
import xlrd
# conn=pymysql.connect(host='192.168.0.222',
#                     port=3306,
#                     user='root',
#                     passwd='112233')
# m=conn.cursor()
# #m.execute('create databases yang;')
# m.execute('use test;')
# #m.execute('show databases;')
# #m.execute('create table qwe(name char(20),age int,sex char(20));')
# #m.execute('insert into qwe values("小龙","10","男");')
# #m.execute('delete from qwe where age=10;')
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[0]
# b=sheet.nrows
# for i in range(b):
#     c=sheet.row_values(i)
#     if i==0:
#         continue
#         m.execute('create table txt({} char(20),{} char(20),{} char(20),{} int)'.format(c[0],c[1],c[2],c[3]))
#     else:
#         m.execute('insert into txt values("{}","{}","{}","{}")'.format(c[0],c[1],c[2],c[4]))
# m.execute('select * from txt;')
# b=m.fetchall()
# print(b)
# import pymysql
# conn=pymysql.connect(host='192.168.0.222',
#                     port=3306,
#                     user='root',
#                     passwd='112233')
# m=conn.cursor()
#m.execute('create databases yang;')
# m.execute('use test;')
#m.execute('show databases;')
#m.execute('create table qwe(name char(20),age int,sex char(20));')
#m.execute('insert into qwe values("小龙","10","男");')
#m.execute('delete from qwe where age=10;')
# f=open('a.txt','r',encoding='utf-8')
# b=f.readlines()
# print(b[0])
# c=b[0]
# for i in range(b):
#     c=sheet.row_values(i)
#     if i==0:
#         continue
#         m.execute('create table txt({} char(20),{} char(20),{} char(20),{} int)'.format(c[0],c[1],c[2],c[3]))
#     else:
#         m.execute('insert into txt values("{}","{}","{}","{}")'.format(c[0],c[1],c[2],c[4]))
# m.execute('select * from txt;')
# b=m.fetchall()
# print(b)




#将a.txt文件导入数据库中
# import pymysql
# with open('a.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# coon=pymysql.connect(host='192.168.0.222',port=3306,user='root',passwd='112233')
# m=coon.cursor()
# m.execute('use test')
# for i in range(len(a)):
#     c=a[i]
#     c=c.split(',')
#     if i==0:
#         m.execute('create table a({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0],c[1],c[2],c[3]))
#     else:
#         m.execute('insert into a values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
# m.execute('select * from a')
# d=m.fetchall()
# print(d)
# coon.close()



#将数据库中的数据导入到txt文档中
# import xlrd
# import pymysql
# conn=pymysql.connect(host='192.168.0.222',port=3306,user='root',passwd='112233')
# m=conn.cursor()
# m.execute('use test;')
# m.execute('select * from txt;')
# b=m.fetchall()
# m.execute('desc txt')
# c=m.fetchall()
# q=[]
# for j in range(len(c)):
#     w=c[j][0]
#     q.append(w)
# b=list(b)
# f=open('a.txt','w',encoding='utf-8')
# for i in range(len(q)):
#     f.write('{},'.format(q[i]))
# f.write('\n')
# for i in range(len(b)):
#     r=len(b[i])
#     g=b[i]
#     for j in range(r):
#         f.write('{},'.format(g[j]))
#     f.write('\n')
# f.close()



#将数据库中的数据导入excel表中
# import xlwt
# import xlrd
# import pymysql
# from xlutils.copy import copy
# conn=pymysql.connect(host='192.168.0.222',port=3306,user='root',passwd='112233')
# m=conn.cursor()
# m.execute('use test;')
# m.execute('select * from txt;')
# b=m.fetchall()
# m.execute('desc txt')
# c=m.fetchall()
# q=[]
# for j in range(len(c)):
#     w=c[j][0]
#     q.append(w)
# b=list(b)
# f=xlrd.open_workbook('b.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# for i in range(len(b)+1):
#     for j in range(len(b[0])):
#         if i == 0:
#
#             sheet.write(0,j,q[j])
#         else:
#             sheet.write(i,j,'{}'.format(b[i-1][j]))
# new_f.save('b.xls')
# conn.close()

#判断本目录下所有的.py文件并打印出来
# import os
# a=os.getcwd()
# # os.chdir(r'F:\学习总结\python')
# # print(os.getcwd())
# # #b=os.popen('ping 192.168.0.1')
# # #print(b.read())
# # print(os.listdir(r'F:\学习总结'))
# #os.mkdir(r'F:\学习总结\aaa')
# #os.rmdir(r'F:\学习总结\aaa')
# #os.makedirs(r'F:\学习总结\aaa\bbb\ccc')
# #os.removedirs(r'F:\学习总结\aaa\bbb\ccc')
# b=os.listdir(r'F:\学习总结\python\untitled1')
# print(b)
# for i in b:
#     c=os.path.isfile(i)
#     w = os.path.splitext(i)
#     if c==True:
#         if w[1]=='.py':
#             print(i)



# def qwe(*a):
#     a=[int(i) for i in a]
#     for i in (1,len(a)):
#         for j in (0,len(a)):
#             if a[j] > a[j+1]:
#                 t = a[j]
#                 a[j] = a[j+1]
#                 a[j+1] = t
#     print(a)
# qwe(2,1,4)
# import paramiko
# with paramiko.SSHClient() as ssh123:
#
#     ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh123.connect(hostname='192.168.0.222',port=22,username='yang',password='123456')
#     while True:
#         q=input('>>>')
#         if q=='exit':
#             break
#         else:
#             a,b,c=ssh123.exec_command(q)
#             print(b.read().decode())
#
#
# qq=paramiko.Transport(('192.168.0.222',22))
# qq.connect(username='yang',password='123456')
# sftp=paramiko.SFTPClient.from_transport(qq)
# sftp.put('day1.py','/etc/day1.py')
# qq.close()
# import smtplib
# import email.mime.multipart as mu
# import email.mime.text as text
# mm='17637839607@163.com'
# yy=['zhaolq1998@163.com','1508295989@qq.com']
# message=mu.MIMEMultipart()
# message['Subject']='python_test'
# message['From']=mm
# message['To']='.'.join(yy)
# txt="""
# 今晚的消费由赵公子买单！！！  尖叫声。。。。。
# """
# tet=text.MIMEText(txt)
# message.attach(tet)
# att1=text.MIMEText(open('b.xls', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="b.xls"'
# message.attach(att1)
#
#
# smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login(mm,'yang1998')
# smtp123.sendmail(mm,yy,message.as_string())


# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('192.168.0.98、',3000))
# while True:
#     qq=input('>>>')
#     if qq=='关闭':
#         sock.close()
#     else:
#         sock.send(qq.encode('utf-8'))
#         ww=sock.recv(1024)
#         print(ww.decode('utf-8'))


# def qwe(x,y):
#     for i in range(len(x)):
#         for j in range(len(x)):
#             if x[i]!=x[j]:
#                 a=x[i]+x[j]
#                 if a==y :
#                     if x[i]>x[j]:
#                         print(x[i],x[j])
# qwe([12,12,13,14,15],27)




# def a(s):
#     s=s[::-1]
#     b=0
#     for i,v in enumerate(s):
#         for j in range(0,10):
#             if v==str(j):
#                 b=b+j*(10**i)
#         return b


#发送邮件 以及附件
#如果需要给多个用户发邮件 就把收件人写成一个集合 然后 message[To]='.'.join(yy)
# import smtplib      #封装smtp协议
# import email.mime.multipart as  mu  #制作邮件
# import email.mime.text as text   #对邮件的正文进行处理
# mm='17637839607@163.com'
# yy=['1508295989@qq.com','17629712980@163.com']
# message=mu.MIMEMultipart()  #创建一个邮件
# message['Subject']='yang_test'  #添加邮件的标题
# message['From']=mm      #添加发件人
# message['To']='.'.join(yy)     #添加收件人
# txt='''新年快乐！'''    #正文内容
# tet=text.MIMEText(txt)   #对正文进行处理
# message.attach(tet)     #将处理过的正文加入到邮件里
# att1=text.MIMEText(open('a.txt','rb').read(),'base64','utf-8')  #添加一个文件
# att1["Content-Type"]='application/octet-stream'     #附件的字段，固定的
# att1["Content-Disposition"]='attachment;filename="b.txt"'  #filename 是给你的附件起一个新的名字
# message.attach(att1)   #将附件添加到邮件中
# smtp666=smtplib.SMTP_SSL('smtp.163.com',465)  #定义邮件服务器
# smtp666.login(mm,'yang1998')         #登录服务器
# smtp666.sendmail(mm,yy,message.as_string())  #发送邮件

#读取文件的内容
# import xlrd
# import xlwt
# f=open('a.txt','r',encoding='utf-8')
# b=f.readlines()
# print(b)
# ff=xlrd.open_workbook('a.xls')
# sheet=ff.sheets()[0]
# for i in range(len(b)):
#     for j in range(len(b)):
#         sheet.write(i,j,b[i])




#基于udp的服务器
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('192.168.0.98',3000))
# while True:
#     client,addr=s.recvfrom(1024)
#     print(client.decode('utf-8'))
#     msg=input('>>>')
#     s.sendto(msg.encode('utf-8'),addr)




# print(hex(123))
# print(oct(123))
# print(bin(123))
# print(int(0b11101))
# a=[chr(i) for i in range(97,103)]
# print(a)
# print(ord(''))
# a=[1,3,7,9,5]
# print(max(a))
# print(min(a))
# print(sum(a))
# a,b=divmod(100,16)
# print(a,b)
# import re
# a=input('>>>')
# b=re.compile('[0-9]{2,}')
# c=b.findall(a)
# print(len(c))
# a=input('>>>')
# c=len(a)
# print(c)
# b=0
# for j in range(c):
#     print(j)
#     for i in range(10):
#         if str(i)==a[j]:
#             b=b+i*10**(c-j-1)
# print(b)
# print(type(b))


#爬虫


import re
import requests
# class FreeBuf():
#     def send_qq(self,page):
#         url='https://www.freebuf.com/page/{}'.format(page)
#
#         res=requests.post(url)
#         hh=res.content.decode('utf-8')
#         return hh
#     def gl(self,x):
#         title=[]
#         patt=re.compile('<div class="news-img">(.*?)<dd>',re.S)
#         itesms=patt.findall(x)
#         for i in itesms:
#             aa=re.findall('title="(.*?)"',i)
#             title.append(aa[0])
#         return title
#     def save(self,y):
#         with open('a.txt','a',encoding='utf-8') as f:
#             for i in y:
#                 f.write(i+'\n')
# fr=FreeBuf()
# for i in range(1,5):
#     hh=fr.send_qq(i)
#     gg=fr.gl(hh)
#     fr.save(gg)


#保存图片
# url='http://www.qiushibaike.com/imgrank/'
# head={
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
# }
# res=requests.post(url,headers=head)
# hh=res.content.decode('utf-8')
# print(hh)
# patt=re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"')
# itesms=patt.findall(hh)
# a=0
# for i in itesms:
#     j='https://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#     msg=requests.get(j,headers=head)
#     hh=msg.content
#     with open('{}.jpg'.format(a),'wb') as f:
#         f.write(hh)
#     a=a+1


# lj = []
# title = []
# class FreeBuf():
#     def send_qq(self,page):
#         url='http://movie.douban.com/top250?start={}&filter='.format(page)
#         head = {
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
#             'Content-Type':'text / html;charset = utf - 8'
#             }
#         res=requests.post(url,headers=head)
#         hh=res.content.decode('utf-8')
#         return hh
#     def gl(self,x):
#          patt=re.compile('<img width="100" alt="(.*)" src="https://img([0-9]+).doubanio.com/view/photo/s_ratio_poster/public/(.*?)jpg" class="">')
#          items=patt.findall(x)
#          for i in range(len(items)):
#              title.append(itesms[i][0])
#              a='https://img'+items[i][1]+'.doubanio.com/view/photo/s_ratio_poster/public/'+items[i][2]+'jpg'
#              lj.append(a)
#          return lj
#     def save(self,y,b):
#         for i in range(len(y)):
#             msg=requests.get(y[i])
#             r=msg.content
#             f=open('{}.jpg'.format(b[i]),'wb')
#             f.write(r)
# fr=FreeBuf()
# hh=fr.send_qq(0)
# gg=fr.gl(hh)
# ss=title
# fr.save(gg,ss)





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
#     client.send(msg.encode('utf-8'))

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


import requests
import json
url='https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&=0&_v=0.80226492&x-zp-page-request-id=f14ab29fd9c84c6987a2d1a82d7259ab-1557219520461-956404'
head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
res = requests.get(url,headers=head)
p=res.content.decode('utf-8')
aa = json.loads(p)
f=open('b.txt','w+',encoding='utf-8')
for  i in range(0,90):
    b1=aa['data']['results'][i]['company']['name']
    b2=aa['data']['results'][i]['jobName']
    b3=aa['data']['results'][i]['salary']
    b4=aa['data']['results'][i]['city']['display']
    b5=aa['data']['results'][i]['eduLevel']['name']
    f.write("{},".format(b1))
    f.write("{},".format(b2))
    f.write("{},".format(b3))
    f.write("{},".format(b4))
    f.write("{}".format(b5))
    f.write('\n')
f=open('b.txt','r',encoding='utf-8')
# a=f.readlines()
# import pymysql
# import xlwt
# ww=xlwt.Workbook('a.xls')
# sheet=ww.add_sheet('zhilian')
# c=["公司ID","岗位名称","薪资","公司地点","学历"]
# for k in range(len(c)):
#     sheet.write(0,k,c[k])
# for l in range(0,len(a)):
#     bb=a[l].split(',')
#     for a1 in range(len(c)):
#         sheet.write(l+1,a1,bb[a1])
# ww.save('a.xls')
# conn=pymysql.connect(host='192.168.0.222',port=3306,user='root',passwd='112233')
# m=conn.cursor()
# m.execute('use test')
# m.execute('create table zhilian(公司ID  char(45),岗位名称 char(35),薪资 char(15),公司地点 char(10),学历 char(10))')
# for j in range(0,len(a)):
#     bb=a[j].split(',')
#     m.execute('insert into zhilian values("{}","{}","{}","{}","{}");'.format(bb[0],bb[1],bb[2],bb[3],bb[4]))

