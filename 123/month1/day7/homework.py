#   5.
# list01=["红桃","黑桃","方片","梅花"]
# list02=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# list_result=[]
# for i in list01:
#     for c in list02:
#         list_result.append((i,c))
# print(list_result)


#   6.
# dict={"R":"红色","G":"绿色","B":"蓝色","A":"透明度"}
# color=input("请输入颜色(RGBA):")
# if color in ["R","G","B","A"]:
#     print(dict[color])
# else: print("颜色不存在")


#   7.
# dict_hobbies = {
#         "qtx": ["看书", "编码", "旅游"],
#         "lzmly": ["刷抖音", "看电影"],
#         "于谦": ["抽烟", "喝酒", "烫头"]
#     }
# # (1)
# print(dict_hobbies["于谦"][1])
# # (2)
# for i in dict_hobbies["qtx"]:
#     print(i)
# # (3)
# for name,interest in dict_hobbies.items():
#     for i in range(len(interest)):
#         print(name,"爱好",interest[i])


#   8.
# dict_travel_info = {
#     "北京": {
#         "景区": ["长城", "故宫"],
#         "美食": ["烤鸭", "豆汁胶圈", "炸酱面"]
#     },
#     "四川": {
#         "景区": ["九寨沟", "峨眉山"],
#         "美食": ["火锅", "兔头"]
#     }
# }
# # (1)
# for city in dict_travel_info:
#     print(city)
# # (2)
# dict_bj_info=dict_travel_info["北京"]
# for i in dict_bj_info["美食"]:
#     print(i)
# # (3)
# for city,dict_info in dict_travel_info.items():
#     for i in dict_info["景区"]:
#         print(city,i)


#   9.
dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}
# (1)
for number,dict_info in dict_employees.items():
    print("%s的员工编号是%d,部门编号是%d,月薪%d元"%(dict_info["name"],number,dict_info["did"],dict_info["money"]))
# (2)
for number,dict_info in dict_employees.items():
    if dict_info["money"]>20000:
        print("%s的员工编号是%d,部门编号是%d,月薪%d元" % (dict_info["name"], number, dict_info["did"], dict_info["money"]))

list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]
# (3)
min_did=list_departments[0]["did"]
for i in range(1,len(list_departments)):
    if list_departments[i]["did"]<list_departments[0]["did"]:
        min_did=list_departments[i]
print("编号最小的部门是:",min_did)
# (4)
for i in range(len(list_departments)-1):
    for c in range(i+1,len(list_departments)):
        if list_departments[i]["did"]>list_departments[c]["did"]:
            list_departments[i],list_departments[c]=list_departments[c],list_departments[i]
print(list_departments)







