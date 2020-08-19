day_of_month=(31,30,28,31,30,31,30,31,31,30,31,30,31,30,31)
month=int(input("输入几月:"))
day=int(input("几日:"))
# day0=0
# for i in range(0,month-1):
#     day0+=(day_of_month[i])
day0=sum(day_of_month[:month-1])
print("这是今年的第",day+day0,"天")

