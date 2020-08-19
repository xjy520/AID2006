"""
    函数式编程 - 语法
        理论支柱 : 函数可以复制给变量,赋值后变量绑定函数
        应用 : 函数赋值给参数
"""
def func01():
    print("func01执行")

# 将函数返回值给变量(None)
# a = func01()

#将函数地址赋值给变量
a = func01
#通过变量调用函数
a()



"""
    函数式编程 - 应用
        "封装" : 将变化点定义到函数中 [分]
        "继承" : 用参数抽象变化 --> 调用参数统一函数的定义 --> 通用函数与具体条件隔离开  [隔]
        "多态" : 调用"父" --> "子"重写(做法满足用法) --> 创建"子"(传递具体条件)       [做]
"""
# list01 = [3,443,4,54,6]
# # 1. 定义函数,获取所有大于10的整数
# def find01():
#     for item in list01:
#         if item > 10:
#             yield item
#
# # 2.定义函数,获取所有小于5的整数
# def find02():
#     for item in list01:
#         if item < 5:
#             yield item
#
#
# # 变化的
# def condition01(item):
#     return item < 5
# def condition02(item):
#     return item > 10
# # 通用的
# def find(condition):
#     for item in list01:
#         if condition(item): #统一
#             yield item


"""
    练习
        1.定义函数,在字典中获取所有房间号小于1003的键值对(元组)
        2.定义函数,在字典中获取姓名长度大于两个字的键值对(元组)
"""
dict01 = {1001: "张无忌", 1002: "赵敏", 1003: "周芷若"}


# def get_room():
#     for i, item in enumerate(dict01.items()):
#         if item[0] < 1003:
#             yield item
#
#
# for i in get_room():
#     print(i)
#
#
# def get_name():
#     for i, item in enumerate(dict01.items()):
#         if len(item[1]) > 2:
#             yield item
#
#
# for c in get_name():
#     print(c)


def find(condition):
    for __, item in enumerate(dict01.items()):
        if condition(item):
            yield item


def condition01(item):
    return item[0] < 1003


def condition02(item):
    return len(item[1]) > 2

for i in find(condition02):
    print(i)
