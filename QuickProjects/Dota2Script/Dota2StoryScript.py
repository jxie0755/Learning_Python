class Hero:
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("\n({} 制造完毕)".format(self.name))
        Hero.population += 1
        print("Greetings, I am {}.".format(self.name))

    def die(self):
        """另一种情况就是机器人死了"""
        print("{} is killed!".format(self.name))
        Hero.population -= 1

        if Hero.population == 0:
            print("Battle was lost. All heroes died!")

    def lastone(self):
        print("{} was the last one standing.".format(self.name))

    def start_fight(self):
        print("{}: '战局为我主导. 胜利已在囊中!一切十拿九稳!'".format(self.name) )

    def kill(self):
        print("{}: '呵呵,这连友谊赛都算不上.'".format(self.name))

    def death_claim_TA(self):
        print("{}: 'My life for Aiur!!'".format(self.name))

    def death_claim_Axe(self):
        print("{}: '斧,斧,斧,斧王不能再斩杀了吗.....'".format(self.name))

    def death_claim_Legion(self):
        print("{}: '我...绝不投降......'".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} heroes now.".format(cls.population))

Legion = Hero("军团指挥官")
Hero.how_many()

Axe = Hero("斧王")
Hero.how_many()

TA = Hero("Templar Assassin")
Hero.how_many()

print("\n -The Battle begins! Defence of the Ancient!!")
Legion.start_fight()

print("\n -Ambushed by 夜魇军团")
TA.die()
TA.death_claim_TA()
Hero.how_many()

print("\n -军团指挥官击杀了暗夜魔王")
Legion.kill()

print("\n -Enemy was pushing hard")
print(" -斧王遭到围剿")
Axe.die()
Axe.death_claim_Axe()
Hero.how_many()

print("\n -Enemy gank succeeded")
Legion.lastone()
Legion.death_claim_Legion()
Legion.die()
