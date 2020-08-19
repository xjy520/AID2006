class Scenario:

    def result(self,things):
        things.damage()


class Things:
    def damage(self):
        pass

class Person(Things):
    def damage(self):
        print("减血")

class Emeny(Things):
    def damage(self):
        print("受伤")

shoulei = Scenario()
person = Person()
emeny = Emeny()
shoulei.result(person)

