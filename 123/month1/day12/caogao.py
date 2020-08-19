class Enemy:
    def __init__(self,hp):
        self.hp = hp

    def damage(self,value):
        self.hp -= value
        print("受伤了")

        if self.hp<=0:
            print("播放死亡动画")

class Player:
    def __init__(self,atk):
        self.atk = atk

    def attack(self,enemy):
        print("揍你")
        enemy.damage(self.atk)

p01 = Player(50)
e01 = Enemy(100)
p01.attack(e01)
p01.attack(e01)
p01.attack(e01)
p01.attack(e01)
p01.attack(e01)