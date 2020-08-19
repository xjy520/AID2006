#   5.
class Skill:
    def __init__(self, name, atk, mp, time):
        self.name = name
        self.atk = atk
        self.mp = mp
        self.time = time

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 2:
            self.__atk = value
        else:
            raise Exception("范围错误")

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, value):
        if 0 <= value <= 80:
            self.__mp = value
        else:
            raise Exception("范围错误")

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        if 0 <= value <= 120:
            self.__time = value
        else:
            raise Exception("范围错误")

skill_infos=Skill("神龙摆尾",1.5,50,10)
print(skill_infos.name)
print(skill_infos.atk)
print(skill_infos.mp)
print(skill_infos.time)


#   6.
# (1)
list_merge = [2, 2, 4, 2]
def zero_to_end():
    for i in list_merge[-1::-1]:
        if i == 0:
            list_merge.remove(i)
            list_merge.append(0)
# zero_to_end(list_merge)
# print(list_merge)

# (2)
def merge():
    for c in range(len(list_merge) - 1, 0, -1):
        if list_merge[c] == list_merge[c - 1]:
            list_merge[c - 1] += list_merge[c]
            list_merge[c] = 0
        zero_to_end()
    if list_merge[0] == list_merge[1]:
        list_merge[0] += list_merge[1]
        list_merge[1] = 0
        zero_to_end()
    # zero_to_end()
    # for i in range (len(list_merge)-1):
    #     if list_merge[i] == list_merge[i+1]:
    #         list_merge[i] += list_merge[i+1]
    #         del list_merge[i+1]
    #         list_merge.append(0)


merge()
print(list_merge)
