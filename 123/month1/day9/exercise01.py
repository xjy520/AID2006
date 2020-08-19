"""
    函数间互相调用
"""
"""
-----------函数-----------
函数1

函数2

函数3
-----------入口------------
"""

#------------------------函数-----------------------------
def get_year(year):
    day_month02 = (29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28)
    return day_month02


def get_total_day(year,month,day):
    day_of_month = [31, get_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = sum(day_of_month[0: month - 1]) + day
    return total_day
#-----------------------入口--------------------------------

year=int(input("输入年份:"))
month=int(input("输入月份:"))
day=int(input("输入天:"))
total_day=get_total_day(year,month,day)
print("%d年%d月%d天是这一年的第%d天"%(year,month,day,total_day))
