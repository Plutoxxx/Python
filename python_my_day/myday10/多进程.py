from multiprocessing import Process
import time, threading

def thread_test():
    t = threading.get_ident()
    print("线程号：%s " % t)
def run(name):
    time.sleep(2)
    print('hello', name)
    t = threading.Thread(target=thread_test, )
    t.start()

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=run, args=('bob %s' % i,))
        p.start()
    # p.join()

