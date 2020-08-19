"""
    练习1 : 在列表中获取所有整数,并计算它的平方
    练习2 : 在列表中获取所有大于10的小数
    要求 : 使用列表推导式,生成器表达式完成
"""
list01 = [4,"a",54.5,True,7,89,1.8]
list02 = [item for item in list01 if type(item) == int]
for i in list02:
    print(i**2)
result02 = (item for item in list01 if type(item) == int)
for c in result02:
    print(c**2)

list03 = [item for item in list01 if type(item) == float and item > 10]
for i in list03:
    print(i)
result03 = (item for item in list01 if type(item) == float and item > 10)
for c in result03:
    print(c)