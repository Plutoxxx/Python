import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://Jack:13222@192.168.50.56/oldboydb",
                       encoding='utf8')

Base = declarative_base()  # 生成orm基类


class User(Base):
    def __repr__(self):
        return "<User(name='%s',  password='%s')>" % (
            self.name, self.password)

    __tablename__ = 'user123'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
#
# Session.commit()  # 现此才统一提交，创建数据

my_user = Session.query(User).filter_by(name='alex').first()
# my_user.name = 'jack'
# my_user.password = '147896'
# print(my_user)
# print(my_user.id, my_user.name, my_user.password)
# Session.commit()

faker_user = User(name='rain', password='957')
Session.add(faker_user)
print(Session.query(User).filter(User.name.in_(['Jack','rain'])).all() )
# Session.rollback()
Session.commit()
print(Session.query(User).filter(User.name.in_(['Jack','rain'])).all() )