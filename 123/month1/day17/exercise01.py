"""
    MyRange1.0
    自定义MyRang类,实现for循环
"""

class MyRange:
    def __init__(self,number):
        self.__number = number

    def __iter__(self):
        return MyRangeIterator(range(self.__number))

class MyRangeIterator:
    def __init__(self,data):
        self.__data = data
        self.__count = -1

    def __next__(self):
        self.__count+=1
        if self.__count >= len(self.__data):
            raise StopIteration
        return self.__data[self.__count]
#
# for number in MyRange(5):
#     print(number)
# itertor = controller.__iter__()
# while True:
#     try:
#         # 2.获取下一个元素
#         item = itertor.__next__()
#         print(item)
#         # 3.停止循环获取
#     except StopIteration:
#         break
# for number in MyRange(99999999999):
#     print(number)



class StudentController:
    def __init__(self):
        self.__list_students = []

    def add_student(self,stu):
        self.__list_students.append(stu)

    def __iter__(self):
        #生成迭代器代码的大致规则:
        # 1.将yield之前的代码放在__next__方法体中
        # 2.将yield之后的数据作为__next__方法返回值
        # print("准备")
        # yield self.__list_students[0]
        # print("准备")
        # yield self.__list_students[1]
        # print("准备")
        # yield self.__list_students[2]
        for item in self.__list_students:
            print("准备数据")
            yield  item


controller = StudentController()
controller.add_student("xx")
controller.add_student("yy")
controller.add_student("zz")

for name in controller:
    print(name)
itertor = controller.__iter__()
while True:
    try:
        # 2.获取下一个元素
        item = itertor.__next__()
        print(item)
        # 3.停止循环获取
    except StopIteration:
        break