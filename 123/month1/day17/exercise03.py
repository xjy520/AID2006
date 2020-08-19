"""
    class generator: #生成器 = 可迭代对象 + 迭代器
        def __iter__(self): #可迭代对象
            return self
        def __next__(self): #迭代器
            准备数据
            返回数据
"""

"""
    练习:
        list01 = []
        定义函数,将全局变量list01中所有奇数返回
        1. 使用传统思想 : 创建新列表存储所有结果,再返回
        2. 使用生成器思想 : 使用yield返回奇数
"""
 #1.
list01 = [5 ,8,746,4652,465,41,12,5,2034,]
def func():
    list02=[]
    for i in list01:
        if i%2!=0:
            list02.append(i)
    return list02

 #2.



def func02():
    for i in list01:
        if i % 2 != 0:
            yield i
result = func02()
for item in result:
    print(item)