"""
    list-->str
    "分隔符".join(列表)
"""
# list_region=[]
# while True:
#     region=input("请输入地区:")
#     if region=="":
#         break
#     list_region.append(region)
# str_region="-".join(list_region)
# print(str_region)

"""
   str-->list
   列表=字符串.split("分隔符")
   
"""
list01="To have a government that is of people by people for people".split(" ")
# list02=[]
# for i in range(len(list01)-1,-1,-1):
#     list02.append(list01[i])
# str_list02=" ".join(list02)
str_list=" ".join(list01[::-1])
print(str_list)