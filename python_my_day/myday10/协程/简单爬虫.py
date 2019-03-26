from urllib.request import urlopen
import gevent,time
from gevent import monkey

monkey.patch_all() # 把当前所有io操作单独做上标记

def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    # f = open("url.html",mode="wb")
    # f.write(data)
    # f.close()
    print('%d bytes received from %s.' % (len(data), url))
urls = ['https://www.cnblogs.com/alex3714/articles/5248247.html',
        'http://gs.jiangnan.edu.cn/',
        'https://github.com/']
# time_start = time.time()
# for url in urls:
#     f(url)
# print("同步运行：",time.time() - time_start)

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.cnblogs.com/alex3714/articles/5248247.html'),
    gevent.spawn(f, 'http://gs.jiangnan.edu.cn/'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步运行：",time.time() - async_time_start)
