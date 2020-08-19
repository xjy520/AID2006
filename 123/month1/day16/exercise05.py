"""
    迭代自定义对象

"""
# class StudentController:
#     def __init__(self):
#         self.__list_students = []
#
#     def add_student(self,stu):
#         self.__list_students.append(stu)
#
#     def __iter__(self):
#         return StudentItertor(self.__list_students)
#
# class StudentItertor:
#     def __init__(self,data):
#         self.data = data
#         self.__count = -1
#     def __next__(self):
#         self.__count += 1
#         if self.__count >= len(self.data):
#             raise StopIteration
#         return self.data[self.__count]
#
#
# controller = StudentController()
# controller.add_student("xx")
# controller.add_student("yy")
# controller.add_student("zz")
#
# for name in controller:
#     print(name)
# itertor = controller.__iter__()
# while True:
#     try:
#         # 2.获取下一个元素
#         item = itertor.__next__()
#         print(item)
#         # 3.停止循环获取
#     except StopIteration:
#         break


class GraphicController:
    def __init__(self):
        self.__list_graphics = []

    def add_graphic(self, graphic):
        self.__list_graphics.append(graphic)

    def __iter__(self):
        return GraphicItertor(self.__list_graphics)

class GraphicItertor:
    def __init__(self,data):
        self.__data = data
        self.__count = -1

    def __next__(self):
        self.__count+=1
        if self.__count >= len(self.__data):
             raise StopIteration
        return self.__data[self.__count]




controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角")
for item in controller:
    print(item)