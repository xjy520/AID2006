#   4.
# list02=[5,1,4,6,7,4,6,8,5]
# number=list02[0]
# for i in range(1,len(list02)):
#     number-=list02[i]
# print("累减结果为:",number)


#   5.
# list_region=[]
# list_people=[]
# for __ in range(5):
#     region=input("请输入疫情地区:")
#     people=int(input("请输入确诊人数:"))
#     list_region.append(region)
#     list_people.append(people)
# print("最大值为:",max(list_people))
# print("最小值为:",min(list_people))
# print("平均值为:",sum(list_people)/len(list_people))


#   6.
# list_year=[year for year in range(1970,2051) if year%4==0 and year%100!=100 or year%400==0]
# print(list_year)


#   7.
list=["我","爱","你","p","y","t","h","o","n",666]
# list_str=list[:-1]
# list_str.append(str(list[-1]))
# str_list="".join(list_str)
# print(str_list)

# str_message="".join([str(item) for item in list])
# print(str_message)


#   8.
# dict={
#   1:"Python语言核心编程",
#   2:"Python高级软件技术",
#   3:"Wed全栈",
#   4:"网络爬虫",
#   5:"数据分析,人工智能"
# }
# course = int(input("请输入课程阶段数"))
# print(dict[course])


#   9.
#(1)
# list = []
# count = 0
# import random
#
# while count < 6:
#     number_red = random.randint(1, 33)
#     if number_red not in list:
#         list.append(number_red)
#         count += 1
# number_blue=random.randint(1,16)
# list.append(number_blue)
# print("中奖号码为:",list)

#(2)
# list=[]
# count=0
# while count<6:
#     number_red=int(input("输入想购买的号码:"))
#     if 1<=number_red<=33 and number_red not in list:
#         list.append(number_red)
#         count+=1
#     elif number_red in list:
#         print("号码已经存在,请重新输入")
#     else:
#         print("号码超过范围,请重新输入")
# while True:
#     number_blue=int(input("输入想购买的号码:"))
#     if 1<= number_blue<=16:
#         list.append(number_blue)
#         break
#     else:
#         print("号码超过范围,请重新输入")
# print(list)


 #   10.
# list=[170,160,180,165]
# number_max=list[0]
# for i in  range(1,len(list)):
#     if number_max<list[i]:
#         number_max=list[i]
# print("最大值为:",number_max=list[i])




