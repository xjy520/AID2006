"""
    实例变量
        在构造函数中定义下列代码
        对象.变量名
        调用 :
            对象.变量名
    实例方法
        在类中定义下列代码
        def 方法名(self)
            方法体
        调用 :
            对象.实例方法()
    总结 : 对象.成员名

    核心价值 : 每一个对象存储一份,可以表达不同对象的不同数据

"""
# class Wife:
#     def __init__(self,name):
#         # 创建实力变量:对象.变量名
#         self.name = name
#
# w01 = Wife("建宁")
# W02 = Wife("双儿")
# # 修改实例变量:对象.变量名 = ?
# w01.name = "建宁公主"
# # 读取实例变量:? = 对象.变量名
# print(w01.name)
# # 系统定义的变量_dict_中,记录着当前对象所有实例变量
# print(w01.__dict__)


class Dog:
    def __init__(self, varieties, nickname, weight, age):
        self.varieties = varieties
        self.nickname = nickname
        self.age = age
        self.weight = weight


    def behavior(self):
        print(self.varieties,"喜欢吃和叫")

d01=Dog("哈士奇","嘻嘻","20","0.5")
d02=Dog("秋田","哈哈","15","1")
d01.behavior()
