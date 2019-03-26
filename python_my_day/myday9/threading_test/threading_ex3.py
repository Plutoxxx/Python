import threading
import time

lock = threading.Lock()
def run(n):
    lock.acquire()
    global num
    num += 1
    time.sleep(0.1)
    lock.release()
num = 0
# t1 = threading.Thread(target=run, args=("t1",))
# t2 = threading.Thread(target=run, args=("t2",))
# t1.start()
# t2.start()

# run(1)
# run(2)
t_obj = []
start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    # t.setDaemon(True) # 把当前线程设置为守护线程
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()

# time.sleep(2)
print("----all threads have finished----")
print("num:", num)
# print("cost:", time.time() - start_time)
