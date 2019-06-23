#定义一个读取txt文件的函数
def read_data():
    with open(r'F:\学习总结\python\untitled5\diesheng\data\a.txt','r') as f:
        d=f.readlines()
        datas=[]
        for i in d:
            datas.append(i.replace('\n','').split(','))
    return datas