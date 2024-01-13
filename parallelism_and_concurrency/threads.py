from threading import Thread
from time import sleep

def my_function():
    sleep(5)

for i in range(0, 5):
    thread = Thread(target=my_function)
    thread.start()
    if thread.is_alive():
        print("Thread running and join will be called")
        thread.join()


def read():
    print("Reading...")
    sleep(4)


threads = []
for i in range(0, 5):
    threads.append(Thread(target=read))
    threads[i].start()

def read_files(records=(0, 100)):
    print("Reading records {n} a {m}".format(n=records[0], m=records[1]))
    sleep(3)


ths = []
for i in range(0, 3):
    n = i * 100
    m = n + 100 - 1
    ths.append(Thread(target=read_files, args=((n, m), )))
    ths[i].start()