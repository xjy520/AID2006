"""


"""

# 需求 : 为功能1/2 增加新功能
# def new_func():
#     print("新功能")
# 外部函数 -- 得旧功能
def new_func(func):
    # 内部函数 -- 包新旧
    def wrapper():
        print("新功能")
        func()
    return wrapper

def func01():
    print("功能1")

@new_func # func02 = new_func(func02)
def func02():
    print("功能2")

# 旧功能 = 新功能
#func01 = new_func
# 旧功能 = 旧功能 + 新功能
# 内部函数 = 调用外部函数
func01 = new_func(func01)

# 调用内部函数 -- 调用wrapper函数
func01()
func02()