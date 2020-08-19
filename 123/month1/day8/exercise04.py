"""
    函数设计理念:
        崇尚小而精,不要大而全
    返回值 :
        函数定义着 给 调用者 传递的信息

        def 函数名()
            ...
            return 数据

        变量 = 函数名()
"""
def usd_to_cny(usd):
    cny = usd * 7.0733
    return cny
result = usd_to_cny(10)
print(result)