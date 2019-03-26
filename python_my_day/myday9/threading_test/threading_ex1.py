import threading
import time

def run(n):
    print("test", n)
    time.sleep(2)
    print("test done", n)

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
    t.setDaemon(True) # 把当前线程设置为守护线程
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()

# time.sleep(2)
print("----all threads have finished----")
print("cost:", time.time() - start_time)
