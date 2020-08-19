"""
    基础算法:
        1.交换变量
            a,b = b,a
        2.计算极值

        3.排序

"""
#   降序:大-->小
#   核心思想:每个元素之间进行比较
# list01=[43,2,45,65,76,8,9]
# for i in range(len(list01)-1):
#     for c in range(i+1,len(list01)):
#         if list01[i]<list01[c]:
#             list01[i],list01[c]=list01[c],list01[i]
# print(list01)

#   升序:小-->大
list01=[43,2,45,65,76,8,9]
for i in range(len(list01)-1):
    for c in range(i+1,len(list01)):
        if list01[i]>list01[c]:
            list01[i],list01[c]=list01[c],list01[i]
print(list01)