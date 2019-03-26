import redis,time
# 1.连接redis
# r =redis.Redis(host="192.168.146.128", port=6379)
# r.set('foo2','bar')
# print(r.get('foo2'))
# 2.连接池
# pool = redis.ConnectionPool(host='192.168.146.128', port=6379)
# r = redis.Redis(connection_pool=pool)
# r.set('foo', 'Bar')
# print(r.get('foo'))
# 3.管道
pool = redis.ConnectionPool(host='192.168.146.128',port=6379)
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline(transaction=False)
pipe.set('name', 'a')
time.sleep(30)
pipe.set('role', 'sb123')
pipe.execute()