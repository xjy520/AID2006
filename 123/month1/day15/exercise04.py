"""
    内置模块 -- 时间
"""
import time

# 1.生活中的时间 - 从公元元年
#   时间元组 : 年,月,日,时,分,秒,星期,年的天,夏令时
print(time.localtime())
tuple_time = time.localtime()
print(tuple_time[1]) # 获取月份

# 2.计算机的时间 - 1970年元旦
#   时间戳 : 一串数字
print(time.time())

# 3.时间戳 --> 时间元组
print(time.localtime(1595237354.8848822))

# 4.时间元组 --> 时间戳
print(time.mktime(tuple_time))

# 5.时间元组 --> 字符串
print(time.strftime("%y/%m/%d %H:%M:%S", tuple_time))
print(time.strftime("%Y/%m/%d %H:%M:%S", tuple_time))

# 6.字符串 --> 时间元组
print(time.strptime("2020/07/20 17:38:36", "%Y/%m/%d %H:%M:%S"))


import time
list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
def get_wday(year,month,day):

    truple = time.strptime("%d/%d/%d"%(year,month,day),"%Y/%m/%d")
    wday = truple.tm_wday
    return list[wday]
year = int(input("输入年份:"))
month = int(input("输入月份:"))
day = int(input("输入日子:"))

print("这天是",get_wday(year,month,day))

