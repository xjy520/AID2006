"""
    内置生成器

"""
# 1. 枚举函数 enumerate
list01 = [4,14,5,12,8,321,42,1]
# for i,item in enumerate(list01):
#     if item > 10:
#         list01[i] = 10
# print(list01)

# 练习1.
# for i,item in enumerate(list01):
#     if item%2== 0:
#         list01[i] = 0
# print(list01)

# 练习2.
dict = {"a":"A","b":"B","c":"C"}
# for i,item in enumerate(dict.items()):
#     print(i,item[0],item[1])
for i,(key,value) in enumerate(dict.items()):
    print(i,key,value)