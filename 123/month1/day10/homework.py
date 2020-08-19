#   3.
class People:
    def __init__(self,name,high,weight,interest):
        self.name = name
        self.high = high
        self.weight = weight
        self.interest = interest


people01 = People("张吴磊", "180", "200", "打游戏")
people02 = People("程祯祥", "183", "140", "睡觉")
people03 = People("王伟汀", "178", "160", "美食")


#   4.
# (1)
class Employess:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


class Departments:
    def __init__(self, did, title):
        self.did = did
        self.title = title


list_employees = [
    Employess(1001, 9002, "师傅", 60000),
    Employess(1002, 9001, "师傅", 50000),
    Employess(1003, 9002, "师傅", 20000),
    Employess(1004, 9001, "师傅", 30000),
    Employess(1005, 9001, "师傅", 15000),
]

list_departments = [
    Departments(9001,"教学部"),
    Departments(9002,"销售部"),
    Departments(9003,"品保部"),
]


def print_employee(emp):
    print("%s的员工编号是%d,部门编号是%d,月薪%d" % (emp.name, emp.eid, emp.did, emp.money))


def print_employee_by_all():
    for emp in list_employees:
        print_employee(emp)


print_employee_by_all()

# (2)
def print_employees_by_gt_2w():
    for emp in list_employees:
        if emp.money > 20000:
            print_employee(emp)

print_employees_by_gt_2w()

# (3)
def get_min_by_did():
    min_value = list_departments[0]
    for i in range(1, len(list_departments)):
        if min_value.did > list_departments[i].did:
            min_value = list_departments[i]
    return min_value


print(get_min_by_did().__dict__)

# (4)
def descending_order_by_did():
    for r in range(len(list_departments) - 1):
        for c in range(r + 1, len(list_departments)):
            if list_departments[r].did < list_departments[c].did:
                list_departments[r], list_departments[c] = list_departments[c], list_departments[r]


descending_order_by_did()
print(list_departments[0].did)


#   5.
class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color


list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]
# (1)

def white_phone():
    list03=[]
    for phone in list_phones:
        if phone.color == "白色":
            list03.append(phone.brand)
    return list03


print(white_phone())


# (2)
def brand_phone():
    for phone in list_phones:
        if phone.brand == "华为2":
            return phone


brand_phone()
print(brand_phone().brand, brand_phone().price, brand_phone().color)


# (3)
list01 = []


def price_phone_below_6000():
    for phone in list_phones:
        if phone.price < 6000:
            list01.append(phone.brand)


price_phone_below_6000()
print(list01)
