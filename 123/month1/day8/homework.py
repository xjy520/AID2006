# # 3.
# def calculate_social_insurance(salary):
#     social_inserance=salary*(0.08+0.02+0.002+0.12)+3
#     return social_inserance
# calculate_social_insurance(input("请输入税前工资"))
# print("税前工资为:",calculate_social_insurance(input("请输入税前工资")))
#
# #   4.
# def calculate_son_high(father_high,mother_high):
#     son_high=(father_high+mother_high)*0.54
#     return son_high

#   5.
# def name_of_course(number):
#
#     course={1:"Python语言核心编程",
#               2: "Python高级软件技术",
#               3:"Web 全栈",
#               4:"网络爬虫",
#               5:"数据分析、人工智能"
#               }
#     return course[number]
#
# name=name_of_course(int(input("输入课程编号:")))
# print(name)
# #
# #   6.
# def life_stage(age):
#     if age < 0:
#         return "年龄输入有误"
#     if age <= 6:
#         return "童年"
#     if age <= 17:
#         return "少年"
#     if age <= 40:
#         return "青年"
#     if age <= 65:
#         return "中年"
#     return "老年"
# age = int(input("请输入年龄："))
# stage=life_stage(age)
# print(stage)
#
# #   7.
# def calculate_discount(account_type,money):
#     if account_type == "vip":
#         if money < 500:
#             return "享受85折扣"
#         return "享受8折扣"
#     if money > 800:
#         return "享受9折扣"
#     return "原价购买"
# discount=calculate_discount("vip",800)
# print(discount)

# #   8.
# def get_max_number(list):
#     max_value=list[0]
#     for i in range(1, len(list)):
#         if max_value < list[i]:
#             max_value = list[i]
# list=[170,160,180,165]
# max_number=get_max_number(list)
# print(max_number)
#
# #   9.
# def ascending_order(list):
#     for i in range(0,len(list)-1):
#         for c in range(i+1,len(list)):
#             if list[i]>list[c]:
#                 list[i],list[c]=list[c],list[i]
# list=[170,160,180,165]
# ascending_order(list)
# print(list)

#   10.
def find_same_element(list):
    for i in range(0,len(list)-1):
        if list[i] in list[i+1:len(list)]:
            return "False"
    return "True"


#   11.
def delete_even_number(list):
    for i in list[0:len(list):1]:
               #for i in range(len(list)-1,-1,-1):
        if i%2==0:
            list.remove(i)
list01=[4,55,6,78,66,22,89,90]
delete_even_number(list01)
print(list01)