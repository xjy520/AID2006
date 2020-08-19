"""
    返回值语法:
        1.返回结果
        2.退出函数(无视循环)
"""
def calculate_cure_ratio(number_of_confirmed,number_of_cure):
    """
        计算治愈比例
    :param number_of_confirmed: 确诊人数
    :param number_of_cure: 治愈人数
    :return: 治愈比例
    """
    cur_ratio = number_of_cure/number_of_confirmed*100
    return cur_ratio

print("治愈比例为",calculate_cure_ratio(100,10),"%")
#print("治愈比例为%d%%"%(calculate_cure_ratio(100,10)))
