# (1)
class Person:
    def __init__(self,name):
        self.name = name

    def clean(self):
        print(self.name,"打扫卫生")
        methods=Methods()
        methods.procter()


class Methods:
    def procter(self):
        print("请保洁")

xm = Person("小明")
xm.clean()

# (2)
class Person:
    def __init__(self, name):
        self.name = name
        self.methods = Methods()

    def clean(self):
        print(self.name, "打扫卫生")
        self.methods.procter()

class methods:
    def procter(self):
        print("请保洁")

xm = Person("小明")
xm.clean()


# (3)
class Person:
    def __init__(self, name):
        self.name = name
    def clean(self,methods):
        print(self.name, "打扫卫生")
        methods.procter()

class methods:
    def procter(self):
        return "请保洁"

methods = Methods()
xm = Person("小明")
xm.clean(methods)