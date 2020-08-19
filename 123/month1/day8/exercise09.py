"""
    定义函数,将数字列表所有偶数,设置为0
    list = [4,55,6,78,66,22,89,90]
           [0,55,0,0,0,0,89,0]
"""
def change_list(list):
    for i in range(0,len(list)):
        if list[i]%2==0:
            list[i]=0
list01 = [4,55,6,78,66,22,89,90]
change_list(list01)
print(list01)


