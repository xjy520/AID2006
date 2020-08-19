"""
    # 创建
    1. 字典名称={键:值,键:值}  键:钥匙 值:内容
    2. 字典名称=dict(其他容器)  其他容器的格式要求:容器元素必须要能一分为二
                            例: dict02=dict([(元素1,元素2),(元素3,元素4)])

    # 添加 字典名称[键] = 值
        注:字典中不存在当前键  若有该键则变为修改

    # 定位 字典名称[键]
          注: 字典中存在当前键

    # 删除 del 字典名称[键]

    #遍历
        for key in 字典名称: --> 得到的是键
        for value in 字典名称.values(): --> 得到的是值
        for key,value in 字典名称.items(): --> 得到键,值
"""
dict01 = {"name":"悟空","sex":"男","money":50000}
for a,b in dict01.items():
    print(a)
    print(b)

dict01 = {"region": "北京", "new": 0, "now": 307, "total": 929, "cure": 613}
dict02 = {"region": "香港", "new": 14, "now": 131, "total": 1299, "cure": 1161}
dict03 = {"region": "上海", "new": 0, "now": 23, "total": 718, "cure": 718}
dict01["dead"] = 9
dict02["dead"] = 7
dict03["dead"] = 7

del dict01["new"]

dict02["new"] = 0

print("%s新增%d,现有%d,累计%d,治愈%d,死亡%d" % (dict03["region"], dict03["new"], dict03["now"], dict03["total"], dict03["cure"], dict03["dead"]))

for key in dict03:
    if dict03[key] == 0:
        print(key)
# for key,value in dict03.items:
#       if value==0:
#           print(key)
print(dict01)
print(dict02)
print(dict03)
