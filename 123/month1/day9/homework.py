#   3.
#
# dict_employees = {
#     1001: {"did": 9002, "name": "师父", "money": 60000},
#     1002: {"did": 9001, "name": "孙悟空", "money": 50000},
#     1003: {"did": 9002, "name": "猪八戒", "money": 20000},
#     1004: {"did": 9001, "name": "沙僧", "money": 30000},
#     1005: {"did": 9001, "name": "小白龙", "money": 15000},
# }
# list_departments = [
#     {"did": 9001, "title": "教学部"},
#     {"did": 9002, "title": "销售部"},
#     {"did": 9003, "title": "品保部"},
# ]
# #   (1)
# def print_info():
#     for number,info in dict_employees.items():
#         print_employees_info(number,info)
#
# def print_employees_info(number,info):
#     print("%s的员工编号是%d,部门编号是%d,月薪%d"%(info["name"],number,info["did"],info["money"]))
#
# print_info()
#
# #   (2)
# def print_salary_below_2w():
#     for number,info in dict_employees.items():
#         if info["money"]>20000:
#             print_employees_info(number,info)
#
# print_salary_below_2w()
#
# #   (3)
# def min_number_departments():
#     for number in range(0,len(list_departments)-1):
#         if list_departments[number]["did"] <= list_departments[0]["did"]:
#             min_numeber=number
#     return min_numeber
#
# min_dapartments=list_departments[min_number_departments()]["title"]
# print(min_dapartments)

#   (4)
# def min_number_descend_departments(list):
#     for i in range(0,len(list)-1):
#         for c in range(i+1,len(list)):
#             if list[i]["did"]<list[c]["did"]:
#                 list[i],list[c]=list[c],list[i]
#
# min_number_descend_departments(list_departments)
# print(list_departments)


#   4.
# list_commodity_infos = [
#     {"cid": 1001, "name": "屠龙刀", "price": 10000},
#     {"cid": 1002, "name": "倚天剑", "price": 10000},
#     {"cid": 1003, "name": "金箍棒", "price": 52100},
#     {"cid": 1004, "name": "口罩", "price": 20},
#     {"cid": 1005, "name": "酒精", "price": 30},
# ]
# list_orders = [
#     {"cid": 1001, "count": 1},
#     {"cid": 1002, "count": 3},
#     {"cid": 1005, "count": 2},
#]
# # (1)
# def print_all_goods_info():
#     for info in list_commodity_infos:
#         print("商品编号%d,商品名称%s,商品单价%d"%(info["cid"],info["name"],info["price"]))

# print_all_goods_info()

# # (2)
# def print_below_2w_goods_info():
#     for info in list_commodity_infos:
#         if info["price"] < 20000:
#             print("商品编号%d,商品名称%s,商品单价%d" % (info["cid"], info["name"], info["price"]))

# print_below_2w_goods_info()

# (3)
# def print_all_order_goods_info():
#     for order_info in list_orders:
#         for all_goods_info in list_commodity_infos:
#             if order_info["cid"]==all_goods_info["cid"]:
#                 print("商品名称%s,商品单价%d,数量%d"%(all_goods_info["name"],all_goods_info["price"],order_info["count"]))
# print_all_order_goods_info()

# (4)
# def most_expensive_goods():
#     for i in range(0,len(list_commodity_infos)-1):
#         if list_commodity_infos[i]["price"]>=list_commodity_infos[0]["price"]:
#             most_expensive_name=list_commodity_infos[i]["name"]
#     return most_expensive_name

# print(most_expensive_goods())

# (5)
# def ascending_price_info():
#     for i in range(0, len(list_commodity_infos) - 1):
#         for c in range(i + 1, len(list_commodity_infos)):
#             if list_commodity_infos[i]["price"] > list_commodity_infos[c]["price"]:
#                 list_commodity_infos[i], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[i]

# ascending_price_info()
# print(list_commodity_infos)


#   5.
#  (1)
message = " 自 强不息,厚 德载 物  "
print(message.count(" "))
