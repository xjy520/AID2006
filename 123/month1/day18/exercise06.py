"""
        使用内置高阶函数实现：
        1. ([1,1],[2,2,2],[3,3,3],[4,4,4,4,4])
           获取元组中长度最大的列表
        2. 在员工列表列表，获取所有员工编号与姓名
        3. 在员工列表中，获取所有工资大于13000的员工
        4. 对员工列表，根据员工编号进行降序排列
        5. 获取所有工资大于15000的员工姓名.
"""
class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


list_employee = [
    EmployeeModel(1001, 9003, "林玉玲", 13000),
    EmployeeModel(1002, 9005, "王荆轲", 16000),
    EmployeeModel(1003, 9003, "刘岳浩", 11000),
    EmployeeModel(1004, 9007, "冯舜禹", 17000),
    EmployeeModel(1005, 9005, "曹海欧", 15000),
    EmployeeModel(1006, 9005, "魏鑫珑", 12000),
]

tuple = ([1,1],[2,2,2],[3,3,3],[4,4,4,4,4])
print(max(tuple,key=lambda item:len(item)))

for i in map(lambda item:(item.eid,item.name) ,list_employee):
    print(i)

for c in filter(lambda item:item.money > 13000,list_employee):
    print(c.__dict__)

result = sorted(list_employee, key=lambda item: item.eid, reverse=True)
for i in result:
    print(i.__dict__)

list = filter(lambda item:item.money > 15000,list_employee)
for i in map(lambda item:item.name,list):
    print(i)