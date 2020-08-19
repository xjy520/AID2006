"""
    闭包
        做法
            1. 有外有内 -- 有剩菜有人吃
            2. 内使用外 -- 人吃剩菜
            3. 外返回内
        字面意思 : 封闭内存空间
        价值 : 将外部函数栈帧执行后保存,不释放,供内部函数使用
"""
def func01():
    a = 10
    def func02():
        print(a)

    # 错误:调用内部函数,返回内部函数的返回值
    # return func02()
    # 返回内部函数
    return func02
#调用外部函数,返回值是内部函数地址
result = func01()
#调用内部函数
result()



"""
    压岁钱
        逻辑连续
"""
def give_gife_money(money):
    """
        获取压岁钱
    """
    print(f"获得了{money}元")
    def child_buy(commdity,price):
        nonlocal money
        money -= price
        print(f"购买了{commdity},花了{price},还剩{money}")
    return child_buy

#利用闭包实现效果
#外部函数调用一次
action = give_gife_money(1000)
#内部函数调用多次
action("变形金刚",300)
action("奥特曼",300)
