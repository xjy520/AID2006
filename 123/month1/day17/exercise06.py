"""
    内置生成器函数
        zip
"""
# list01 = [1,2,3]
# list02 = [4,5,6]
# for item in zip(list01,list02):
#     print(item)

# 矩阵转置
map = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
map01 = []
# for item in zip(map[0],map[1],map[2],map[3]):
for item in zip(*map):
    map01.append(list(item))
print(map01)

#  列表推导式
list01 = [3,4,2,8,40,1,6]
list02 = [item for item in list01 if item > 5]
print(list02)

#   生成器表达式
# def func():
#     for item in list01:
#         if item > 5:
#             yield item

result = (item for item in list01 if item > 5)   #生成器表达式
# result = func()
for item in result:
    print(item)
