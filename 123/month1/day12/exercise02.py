class Person:
    def __init__(self, name):
        self.name = name

    def work(self, money):
        print(self.name, "工作挣了%d元" % money)

    def teach(self,other,skill):
        print("%s教%s%s" % (self.name,other.name, skill))

zwj = Person("张无忌")
zwj.work(5000)
zm = Person("赵敏")
zm.work(10000)
zwj.teach(zm, "九阳神功")

