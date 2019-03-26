class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating......"%self.name)

    def sleep(self):
        print("%s is sleeping......"%self.name)

    def talk(self):
        print("%s is talking......"%self.name)

class Relation(object):
    def makefriends(self, obj):
        print("%s is making friend with %s" % (self.name, obj.name))

class Man(People, Relation): # 多继承
    def __init__(self, name, age, money):
        # People.__init__(self, name, age) # 方法1进行重构
        super(Man, self).__init__(name, age) # 方法2进行重构
        self.money = money
        print("%s 出生带。。%s元。。" % (self.name,self.money))
    def piao(self):
        print("%s is piaoing.....50s....done"%self.name)

class Women(People):
    def birth(self):
        print("%s is broning..."%self.name)

m = Man("老陈", 20, 10)
m.eat()
m.piao()
w = Women("老黄", 20)
w.birth()
m.makefriends(w)