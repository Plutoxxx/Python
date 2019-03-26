import threading,time

event = threading.Event()

def light():
    count = 0
    event.set()
    while True:
        if count > 5 and count < 10:
            print("\033[41;1m read light is on ...\033[0m")
            event.clear()
        elif count > 10:
            count = 0
            event.set()
        else:
            print("\033[42;1m green light is on ...\033[0m")
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print("[%s] is running" % name)
            time.sleep(1)
        else:
            print("[%s] is waiting" % name)
            event.wait()


light1 = threading.Thread(target=light,)
light1.start()
car1 = threading.Thread(target=car,args=("TESL",))
car1.start()