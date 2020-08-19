def rectangular(wide,long,char):
    """

    :param wide:
    :param long:
    :param char:
    :return:
    """
    for r in range(wide):
        for c in range(long):
            print(char,end=" ")
        print()
rectangular(3,5,"#")
rectangular(2,4,"*")

"""
    定义 : 1. 用于封装一个特定的功能,表示一个功能或者行为
          2. 函数是一个重复可以执行的语句块
"""




