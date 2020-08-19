def calculate_jin_liang(weight):
    """
        计算几斤几两
    :param weight:重量为多少两
    :return: 几斤几两
    """
    jin=weight//16
    liang=weight%16
    result=[jin,liang]
    return result
print("%d斤%d两"%(calculate_jin_liang(50)[0],calculate_jin_liang(50)[1]))


def calculate_iq_level(iq):
    """
        计算智商等级
    :param iq: 智商
    :return: 等级
    """
    if iq >= 140:
        return ("天才")
    if iq >= 120:
        return ("超常")
    if iq >= 110:
        return ("聪慧")
    if iq >= 90:
        return ("正常")
    if iq >= 80:
        return ("迟钝")
    return ("低能")
print(calculate_iq_level(150))