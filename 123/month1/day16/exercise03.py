"""
    主动抛出异常:
        目的 : 快速传递错误消息
        做法 :
            1.抛出方:
                raise xxxx(错误消息)
            2.接收方:
                try:
                    ...
                except xxxx as e:
                    ...
    练习:创建敌人类,保障攻击力在0 -- 100之间
"""
class Enemy:
    def __init__(self,atk):
        self.atk = atk
    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise Exception("攻击范围出错","0 <= value <= 100")

while True:
    try:
        atk = int(input("请输入攻击力"))
        attrack = Enemy(atk)
        print(attrack.atk)
        break
    except Exception as e:
        print(e)
