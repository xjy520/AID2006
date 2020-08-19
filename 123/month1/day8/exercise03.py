def print_list(list):
    """
        打印二维列表
    :param list: 输入二维列表
    :return:
    """
    for i in list:
        for c in i:
            print(c,end="\t")
        print()
list01=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
]

print_list(list01)

