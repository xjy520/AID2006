"""
    玩家 攻击 敌人,敌人播放受伤动画
"""
class Figure:
    def __init__(self,camp):
        self.camp = camp
    def attack(self,other,behavior):
        print(self.camp+"攻击"+other.camp)
        print(other.camp,end="")
        behavior.be()

class Behavior:
    def be(self):
        print("播放受伤动画")
player = Figure("玩家")
enemy = Figure("敌人")
behavior = Behavior()
player.attack(enemy,behavior)
