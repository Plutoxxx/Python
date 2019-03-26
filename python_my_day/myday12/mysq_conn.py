import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.50.56', port=3306, user='Jack', passwd='13222', db='oldboydb')
# 创建游标
cursor = conn.cursor()

data = [
    ('alex', '2', '2019-3-8', 'M'),
    ('ChenRonghua', '33', '2018-6-18', 'M'),
    ('sacbnk', '5', '2016-3-3', 'F')
]
# 执行SQL，并返回收影响行数
# effect_row = cursor.execute("select * from student")
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

cursor.executemany("insert into student(name,age,register_data,sex)values(%s,%s,%s,%s)", data)
conn.commit()
