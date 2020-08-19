#   3.

# import time
# list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
# def get_wday(year,month,day):
#
#     truple = time.strptime("%d/%d/%d"%(year,month,day),"%Y/%m/%d")
#     wday = truple.tm_wday
#     return list[wday]
# year = int(input("输入年份:"))
# month = int(input("输入月份:"))
# day = int(input("输入日子:"))
#
# print("这天是"+get_wday(year,month,day))


#   4.
list_merge = []
map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]

class Game2048Model:
    def __init__(self,list_merge,map):
        self.list_merge = list_merge
        self.map = map

class Game2048View:
    def __init__(self):
        self.contort = Game2048Controller()
    def move_merge(self):
        direct = input("按wsad移动:")
        if direct == "w":
            return self.contort.move_up()
        if direct == "s":
            return  self.contort.move_down()
        if direct == "a":
            return  self.contort.move_left()
        if direct == "d":
            return  self.contort.move_right()
    def display_merge(self):
        for i in map:
            for c in i:
                print(c, end="  ")
            print()

    def main(self):
        self.display_merge()
        while True:
            # game = Game2048View()
            # game.move_merge()
            # game.display_merge()
            self.move_merge()
            self.display_merge()


class Game2048Controller:
    def __zero_to_end(self):
        for item in list_merge:
            if item == 0:
                list_merge.remove(item)
                list_merge.append(0)
        for i in range(len(list_merge) - 1):
            if list_merge[i] == list_merge[i + 1]:
                list_merge[i] += list_merge[i + 1]
                del list_merge[i + 1]
                list_merge.append(0)

    def move_left(self):

        global list_merge
        for line in map:
            list_merge = line
            self.__zero_to_end()



    def move_right(self):

        global list_merge
        for line in map:
            list_merge = line[::-1]
            self.__zero_to_end()
            line[::-1] = list_merge

    def square_matrix_transposition(self):
        for c in range(1, len(map)):
            for r in range(c, len(map)):
                map[r][c - 1], map[c - 1][r] = map[c - 1][r], map[r][c - 1]

    def move_up(self):
        self.square_matrix_transposition()
        self.move_left()
        self.square_matrix_transposition()

    def move_down(self):
        self.square_matrix_transposition()
        self.move_right()
        self.square_matrix_transposition()

    # def print_merge(self):
    #     for i in map:
    #         for c in i:
    #             print(c,end="  ")
    #         print()


view = Game2048View()
view.main()
