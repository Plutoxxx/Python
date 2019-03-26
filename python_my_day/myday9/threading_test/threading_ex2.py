import threading
import time

def run(n):
    print("test", n)
    time.sleep(2)


class MyThreading(threading.Thread):
    def __init__(self, n):
        super(MyThreading, self).__init__()
        self.n = n
    def run(self):
        print("runing threading", self.n)
        time.sleep(2)

t1 = MyThreading("t1")
t2 = MyThreading("t2")
t1.start()
t2.start()

# run(1)
# run(2)
