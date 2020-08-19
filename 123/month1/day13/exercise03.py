
class GraphicManager:
    def __init__(self):
        self.list_graphic = []

    def add_graphic(self,graphic):
        self.list_graphic.append(graphic)

    def calculate_total_area(self):
        total_area = 0
        for i in self.list_graphic:
            total_area += i.calculat_area()
        return total_area

class Graphic:

    def calculat_area(self):
        pass

class Round(Graphic):
    def __init__(self,r):
        self.r = r

    def calculat_area(self):
        s = 3.14*self.r**2

manager = GraphicManager()
manager.add_graphic(Round(5))
print(manager.calculate_total_area)