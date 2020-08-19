"""
    迭代器 --> yield
    练习:将迭代器版本的图形管理器改为yield版本实现

    练习2:将MyRange版本改为yield版本实现
"""

class GraphicController:
    def __init__(self):
        self.__list_graphics = []

    def add_graphic(self, graphic):
        self.__list_graphics.append(graphic)

    def __iter__(self):
        for item in self.__list_graphics:
            yield item


controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角")
for i in controller:
    print(i)



class MyRange:
    def __init__(self,number):
        self.__number = number
    def __iter__(self):
        # for item in range(self.__number):
        number0 = 0
        while number0 < self.__number:
            yield number0
            number0+=1

for i in MyRange(10):
    print(i)


