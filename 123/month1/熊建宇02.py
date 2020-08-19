#   1.
class Human:
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel

m = Human("tom",45,"12333333333")
print(m.name)
print(m.age)


#   2.
class Hotel:
    def __init__(self,room,cf,br):
        self.room = room
        self.cf = cf
        self.br = br
    def amount(self,day):
        price = (self.room * self.cf + self.br)*day
        return price
h1 = Hotel(200,1.0,15)
h2 = Hotel(150,0.9,8)
H1 = h1.amount(3)
H2 = h2.amount(6)


#   3.

def list_ascending_order(list):
    for i in range(0,len(list)-1):
        for c in range(i+1,len(list)):
            if list[i]>list[c]:
                list[i],list[c]=list[c],list[i]



#   4.
x = [
    [13,4,7],
    [5,7,9],
    [4,5,2]]

y = [
     [1, 3, 4],
     [3, 1, 5],
     [7, 4, 8]]

list_new = []
for i in range(3):
    list_z = []
    for c in range(3):
       z = x[i][c]+ y[i][c]
       list_z.append(z)
    list_new.append(list_z)
print(list_new)



#   5.
def print_pattern(wide,long):
    for r in range(wide):
        for c in range(long[r]):
            print("*",end="")
        print()
print_pattern(5,[1,3,5,3,1])




#   6.
def total(day):
    if day >= 3:
        total_pich = 3 * 2**(day-1)-2
        return total_pich
    if day == 2:
        return 4
    if day == 1:
        return 1
day = 10
print(total(day))






