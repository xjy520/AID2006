"""
    函数--功能
        参数 : 用法     向     做法  传递的信息
        制作
            def 函数名称():
                函数体
        使用
    做法 + 用法 --> 缺点:做法变化,需要修改多次
"""
# 做法
# 形式参数 : 表面数据
def attack(count):
    for __ in range(count):
        print("临门一脚")
        print("摆拳")
        print("勾拳")
# 实际参数 : 具有真实数据
# 用法
attack() #调试如果希望审查函数体代码,按F7


"""
    创建函数,打印列表所有元素(一行一个)
"""
def print_list_elements(list):
    for item in list:
        print(item)
list01=[1,2,3,4]
list02=[5,65,76,8,90]
print_list_elements(list01)
print_list_elements(list02)
