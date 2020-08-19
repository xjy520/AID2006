#   3.
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 280:
            self.__speed = value

class ElectricCar(Car):
    def __init__(self,brand,speed,battery,power):
        self.battery = battery
        self.power = power
        super().__init__(brand,speed)

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        if 0 <= value <= 50000:
            self.__battery = value

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if 200 <= value <= 250:
            self.__power = value

    def __str__(self):
        return "%s的车,速度为%d,电池容量为%d,充电功率为%d"%(self.brand,self.speed,self.battery,self.power)

e01 = ElectricCar("特斯拉",250,40000,220)
print(e01)



#   4.
# (1)
# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def call(self):
#         methods.telphone()
#         print(self.name+methods.telphone()+"打电话")
#
# class Methods:
#     def telphone(self):
#         return "用手机"
#
# methods = Methods()
# xm = Person("小明")
# xm.call()


# (3)
class Enemy:
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("受伤了")
        if self.hp <= 0:
            print("播放死亡动画")


class Player:
    def __init__(self, atk):
        self.atk = atk

    def attack(self, enemy):
        print("揍你")
        enemy.damage(self.atk)
        # 通过类名调用
        # Enemy().damage(self.atk)

p01 = Player(50)
e01 = Enemy(100)
p01.attack(e01)











#   5.
# (3)
# list_merge = [2, 2, 4, 2]


# def zero_to_end():
#     for i in list_merge[-1::-1]:
#         if i == 0:
#             list_merge.remove(i)
#             list_merge.append(0)


# def merge():
#     for c in range(len(list_merge) - 1, 0, -1):
#         if list_merge[c] == list_merge[c - 1]:
#             list_merge[c - 1] += list_merge[c]
#             list_merge[c] = 0
#         zero_to_end()
#     if list_merge[0] == list_merge[1]:
#         list_merge[0] += list_merge[1]
#         list_merge[1] = 0
#         zero_to_end()
#
# merge()
# print(list_merge)

# (4)
# def zero_to_end():
#     for i in list_merge:
#         if i == 0:
#             list_merge.remove(i)
#             list_merge.insert(0,0)
#
# def merge():
#     for c in range(0, len(list_merge)-2):
#         if list_merge[c] == list_merge[c + 1]:
#             list_merge[c + 1] += list_merge[c]
#             list_merge[c] = 0
#         zero_to_end()
#     if list_merge[-2] == list_merge[-1]:
#         list_merge[-1] += list_merge[-2]
#         list_merge[-2] = 0
#         zero_to_end()
#
# merge()
# print(list_merge)