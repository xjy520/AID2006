#   4.
class Person:
    def __init__(self,name):
        self.name = name


    def call(self, communication):
        print(self.name, "打电话")
        communication.dialing()

class Communication:
    def dialing(self):
        pass


class MobilePhone(Communication):
    def dialing(self):
        print("用手机")

class LandLine(Communication):
    def dialing(self):
        print("用座机")

class SatellitePhone(Communication):
    def dialing(self):
        print("用卫星电话")


xm = Person("小明")
xm.call(MobilePhone())


#   5.
class EmployeeManager:
    def __init__(self):
        self.list_employee = []

    def employee(self,work):
        self.list_employee.append(work)

    def salary(self):
        total_salary = 0
        for i in self.list_employee:
            total_salary += self.work.salary
        return total_salary

class Work:
    def salary(self):
        pass

class Programmer(Work):
    def __init__(self,base_salary,project_share):
        self.base_salary = base_salary
        self.project_share = project_share
    def salary(self):
        return self.base_salary+self.project_share

class Tester(Work):
    def __init__(self,base_salary,bug_number):
        self.base_salary = base_salary
        self.bug_number = bug_number

    def salary(self):
        return self.base_salary+self.bug_number*5

employeeManager = EmployeeManager()
employeeManager.employee(Programmer(10000,25000))
employeeManager.employee(Tester(15000,1000))
print(employeeManager.salary)




#   6.
# class Player:
#     def __init__(self,atk):
#         self.atk = atk
#
#     def attack(self,target):
#         # 对象.实例方法(参数)
#         target.damage(self.atk)
#
# class Enemy:
#     def __init__(self,hp):
#         self.hp = hp
#
#     def damage(self,value):
#         print("额,受伤")
#         self.hp -= value
#         if self.hp <=0:
#             # 对象.实例方法()
#             self.death()
#
#     def death(self):
#         print("播放死亡动画")
#
# p01 = Player(50)
# e01 = Enemy(100)
# p01.attack(e01)
# p01.attack(e01)
# """
#
#
#     (4)敌人还能攻击玩家,玩家受伤(减血+碎屏)后可能死亡(游戏结束)
#         # 缺点1：两个类代码重复度高
#         # 缺点2：两个类紧耦合
# """
# class Player:
#     def __init__(self, hp, atk):
#         self.hp = hp
#         self.atk = atk
#
#     def attack(self, target):
#         # 对象.实例方法(参数)
#         target.damage(self.atk)
#
#     def damage(self, value):
#         print("碎屏")
#         print("额,受伤")
#         self.hp -= value
#         if self.hp <=0:
#             self.death()
#
#     def death(self):
#         print("游戏结束")
#
#
# class Enemy:
#     def __init__(self, hp, atk):
#         self.hp = hp
#         self.atk = atk
#
#     def damage(self, value):
#         print("头顶爆字")
#         print("额,受伤")
#         self.hp -= value
#         if self.hp <= 0:
#             # 对象.实例方法()
#             self.death()
#
#     def death(self):
#         print("播放死亡动画")
#
#     def attack(self, target):
#         target.damage(self.atk)






