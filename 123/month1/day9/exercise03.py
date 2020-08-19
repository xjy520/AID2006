#----默认形参
# def calculate_second(hour=0, minute=0, second=0):
#     total_second = 3600 * hour + 60 * minute + second
#     print(total_second)
#
#
# calculate_second(1, 20, 55)
# calculate_second(minute=40, second=40)
# calculate_second(2, second=50)
# calculate_second(minute=14)


#----星号元祖形参
# def multiplication_total(*args):
#     result = 1
#     for i in args:
#         result *= i
#     return result


"""
    调用下列函数
"""
def func01(*args,**kwargs):
    print(args)
    print(kwargs)

func01(1,2,3,4,5,p1=9,p2=8,p3=7)
list=[1,2,3]
dict={"a":1,"b":2}
func01(*list,dict)
func01(**dict)

# 位置形参   星号元组形参   命名关键字形参   双星号字典形参
def func02(p1,p2,*args,p3,p4=4,**kwargs):
    print(p1)
    print(p2)
    print(args)
    print(p3)
    print(p4)
    print(kwargs)
#   位置实参,关键字实参
func02(1,2,"dasda","dasdas","wqwewq",p3=3,p4=8,s1=451,s2=748,s3=41125)
#func02(p1=1,p2=2,3,4,5,6,) ---> 错