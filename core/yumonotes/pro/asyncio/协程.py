# 进程 》 线程 》 协程
import threading
import multiprocessing
import time


def func_0():
    for i in range(100):

        print("func 0", i)


def func_1():
    for i in range(100, 200):
        print("func 1", i)

start0 = time.time()
func_1()
func_0()
end0 = time.time()

start1 = time.time()
t1 = threading.Thread(func_0())
t2 = threading.Thread(func_1())

t1.start()
t2.start()
end1 = time.time()

print(start0 - end0)
print(start1 - end1)

