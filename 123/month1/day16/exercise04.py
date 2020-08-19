"""
    迭代iteration : 依次获取获取容器每个元素
    可迭代对象iterable : 能够返回迭代器
    迭代器iterator : 做迭代的工具
"""
message = "我是齐天大圣孙悟空"
# for 循环原理
# 1.获取迭代器对象
itertor = message.__iter__()
while True:
    try:
        # 2.获取下一个元素
        item = itertor.__next__()
        print(item)
        # 3.停止循环获取
    except StopIteration:
        break

# 笔试题 : 能够参与for循环的条件是什么?
# 答 : 对象能够获取迭代器对象

# 机试题 : 不用for循环,获取字典所有键值对
dict01 = {"a":"A","b":"B","c":"C"}
itertor = dict01.items().__iter__()
while True:
    try:
        item = itertor.__next__()
        print(item)
    except StopIteration:
        break
# for key,value in dict01.items():
#     print(key,value)