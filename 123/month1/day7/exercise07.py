dict_commodity_infos={
    1001:{"name":"屠龙刀","price":10000},
    1002:{"name":"倚天剑","price":10000},
    1003:{"name":"金箍棒","price":52100},
    1004:{"name":"口罩","price":20},
    1005:{"name":"酒精","price":30}
}
for key,value in dict_commodity_infos.items():
    print("商品编号%d,商品名称%s,商品单价%d"%(key,value["name"],value["price"]))



list_orders=[
    {"cid":1001,"count":1},
    {"cid":1002,"count":3},
    {"cid":1005,"count":2}
]
dict_max=list_orders[0]
for i in range(1,len(list_orders)):
    if dict_max["count"]<list_orders[i]["count"]:
        dict_max=list_orders[i]
print(dict_max)


for i in range(len(list_orders)-1):
    for c in range(i+1,len(list_orders)):
        if list_orders[i]["count"]<list_orders[c]["count"]:
            list_orders[i],list_orders[c]=list_orders[c],list_orders[i]
print(list_orders)
