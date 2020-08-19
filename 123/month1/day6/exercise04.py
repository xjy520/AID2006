"""
   列表推导式
     格式:  [item for 变量 in 容器 if item>5]
     例子:  list02=[item for in list01 if item>5]
           # 将list01中大于5的添加到list02中
"""
#生成1-50之间能被3或者5整除的数字
# list01=[]
# number=0
# for __ in range(0,50):
#     number+=1
#     list01.append(number)
list02=[item for item in range(1,51) if item%3==0 or item%5==0]
print(list02)

#生成5-100之间的数字平方
list=[item ** 2 for item in range(5,101)]
print(list)

