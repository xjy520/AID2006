"""
    字典推导式
        字典名称={键:值 for 变量 in 容器 if 条件}
"""
# dict={}
# for number in range(1,11):
#     dict[number]=number**2
# print(dict)
#
# dict={number:number**2 for number in range(1,11)}

list_name=["张无忌","赵敏","周芷若"]
list_room=[101,102,103]
# dict01={
#         list_room[0]:list_name[0],
#         list_room[1]:list_name[1],
#         list_room[2]:list_name[2]
#         }
dict01={list_room[i]:list_name[i] for i in range(3)}
# dict02={}
# for key,value in dict01.items():
#     dict02[value]=key
dict02={value:key for key,value in dict01.items()}
print(dict01)
print(dict02)
