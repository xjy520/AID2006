"""
    继承
        编程:子类不用写,但是能直接用
"""
#多个类型,有行为上的共性,在概念上是一致的
class Person:
    def say(self):
        print("说话")


class Student(Person):

    def study(self):
        print("学习")
        self.say()


class Teacher(Person):
    def teach(self):
        print("教学")
        self.say()

# 子类可以访问父类
s01 = Student()
s01.study()
# 父类只能访问父类
p01 = Person()
p01.say()

#
# # 1. isinstance(学生对象 , 类型)
# # 学生对象 是一种 学生类型
# print(isinstance(s01,Student))
# print(isinstance(s01,Person))
# print(isinstance(p01,Student))
#
# # 2. isinstance(类型 , 类型)
# # 学生类型 是一种 学生类型
# print(issubclass(Student,Student))
#print(issubclass(Student,Person))
# print(issubclass(Person,Student))
#
# # 1. type(对象) == Student
# print(type(s01) == Student)
# print(type(s01) == Person)
# print(type(p01) == Student)

#------------------------练习-------------------
class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def run(self):
        print("跑")
        self.eat()


class Bird(Animal):
    def fly(self):
        print("飞")
        self.eat()

gou = Dog()
bird = Bird()
animal = Animal()
print(isinstance(gou,Animal))
print(isinstance(gou,Bird))
print(isinstance(bird,Animal))
print(issubclass(Dog,Animal))
print(issubclass(Bird,Animal))
print(issubclass(Animal,Dog))
