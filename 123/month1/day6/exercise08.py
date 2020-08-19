"""
    字典 - 基础操作
    可变容器

"""
#   1.创建    字典名称={键:值,键:值}  键:钥匙 值:内容
# dict01 = {"name":"悟空","sex":"男","money":50000}

#   2.添加    字典名称[键]=值
# dict01["age"] = 22

#   3.定位    通过键找对应的值
# print(dict01["name"])


dict01={"region":"北京","new":0,"now":320}
dict02={"region":"香港","new":17,"now":121}
dict03={"region":"上海","new":2,"now":23}
dict01["dead"]=9
dict02["dead"]=7
dict03["dead"]=7
#print(dict01["region"],"新增人数为",dict01["new"],",现有人数为",dict01["now"],",死亡人数为",dict01["dead"])
#print(dict02["region"],"新增人数为",dict02["new"],",现有人数为",dict02["now"],",死亡人数为",dict02["dead"])
#print(dict03["region"],"新增人数为",dict03["new"],",现有人数为",dict03["now"],",死亡人数为",dict03["dead"])
print("%s新增人数为%i,现有人数为%i,死亡人数为%d"%(dict01["region"],dict01["new"],dict01["now"],dict01["dead"]))
print("%s新增人数为%i,现有人数为%i,死亡人数为%d"%(dict02["region"],dict02["new"],dict02["now"],dict02["dead"]))
print("%s新增人数为%i,现有人数为%i,死亡人数为%d"%(dict03["region"],dict03["new"],dict03["now"],dict03["dead"]))