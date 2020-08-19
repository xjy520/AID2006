list_merge = []
map = [[4,0,2,4],
       [2,2,4,2],
       [0,4,2,2],
       [8,4,2,2]
       ]
class Game2048Modle:
    def __init__(self,map,list_merge):
        self.map = map
        self.list_merge = list_merge

class Game2048View:
    def __init__(self):
        self.contorl = Game2048Controller()

class Game2048Controller:
    def zero_to_end(self):
