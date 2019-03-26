class Dog(object):
    """这个类是来描述狗这个对象的"""
    def __init__(self,name):
        self.name = name

    #@staticmethod# 加了之后下边的函数实际上和类已经没有关系了
    #@classmethod
    def eat(self, food):
        print("%s is eating %s" % (self.name, food))

    @property
    def talk(self):
        print("%s is talking"%self.name)

    def __call__(self, *args, **kwargs):
        print("i am coming", args, kwargs)

    def __str__(self):
        return "yt"
# print(Dog.__dict__) #打印类中所有属性，不打印实例属性
d = Dog("Chengronghua")
# print(d.__dict__) #打印类中实例属性，不打印类属性
#d.eat(d, "包子")#静态方法时调用
# d.talk
# print(d.__doc__)
# d(1,2,3,name=3)
print(d)
