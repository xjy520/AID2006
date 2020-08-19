 # 扩容机制:
 #     1.开辟更大空间
 #     2.拷贝原始数据
 #     3.替换内存地址

#   1.创建
#     --元组名 = (元素1,元素2,元素3)
#     --元祖名 = tuple(其他容器)
# tuple01 = (10, 20,30)

#   2.定位
#   -- 索引 元组名[整数]
# print(tuple01[0])   #获取第一个元素

#   --切片 元组名[开始:结束:间隔]
#     备注:创建新元组
# print(tuple01[-2:])

#   3.遍历
#   --for 变量 in 元组名
# for item in tuple01:
#     print(item)
#   --for 变量 in range():
# for i in range(len(tuple01)-1,-1,-1)
#     print(tuple01(i))

#   4.特殊:
#   --小括号可以省略
# tuple = "a","b"
#   --拆包    变量1,变量2 = 容器
#data01,data02=(10,20)
# data01,data02="ab"
# data01,data02=[10,20]
#   --如果元组中只有一个元素,需要添加逗号    tuple=(10,)