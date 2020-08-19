
# c = int(input("输入行数:"))
# list = [None]*(c)
# list_i = []
# for i in range(2,c-2):
#     for r in range(1,c-1):
#         list_i.append(list[i-1][r-1]+list[i-1][r])
#     list.append(list_i)
#
# print(list)




#
# a = "5+(5-(5+4))"
# print(type(eval(a)))

# 计算水仙花数
list = []
a = int(input("输出位数"))
for i in range(10**(a-1),10**a-1):
    number = 0
    for c in range(a):
        number += ((i//(10**c))%10)**3
    if number == i:
        list.append(i)
print(list)

# 二分查找
def func(i,list):
    for c in range(len(list)):
        if list[c] == i:
            return c
    if i < list[0]:
        return 0
    for r in range(1,len(list)):
        if list[r] > i and list[r-1] < i:
            return r
print(func(8,[1,2,6,8,9]))
print(func(5,[1,2,6,8,9]))

# 对字典升序排列
def order_dict(dict,list):
    for i,item in enumerate(dict.items()):
        list.append(item)
    for c in range(len(list)-1):
        for r in range(c+1,len(list)):
            if list[c][1] > list[r][1]:
                list[c],list[r] = list[r],list[c]
dict = {"张无忌":201,"赵敏":101,"小昭":105,"周芷若":302}
list = []
order_dict(dict,list)
print(list)


