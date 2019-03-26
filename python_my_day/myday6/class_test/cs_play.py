class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value  # 私有变量
        self.money = money

    def shot(self):
        self.__buy_gun()
        print("shooting...")

    def got_shot(self):
        self.__life_value -= 10
        print("%s ah...,I got shot..." % self.name)

    def __buy_gun(self):     # 私有函数
        print("just bought %s" % self.weapon)

    def info(self):
        print("name:%s weapon:%s life_value:%s" % (self.name,
                                                   self.weapon,
                                                   self.__life_value))

    def __del__(self):
        print("%s 哦，彻底死了。。。" % self.name)


r1 = Role('Alex', 'police', 'AK47') # 生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色
r1.shot()
r1.info()
r1.got_shot()
r1.info()
# r1.__buy_gun()

