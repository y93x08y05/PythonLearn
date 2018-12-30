#  -*- coding : utf-8 -*-
import time
import threading


def print_nums(s):
    for i in range(5):
        time.sleep(1)
        print("线程", s, ":", i)


class MyThread(threading.Thread):
    def __init__(self, s):                     # 构造函数
        threading.Thread.__init__(self)
        self.s = s

    def run(self):                             # 执行函数
        print_nums(self.s)

if __name__ == "__main__":
    thread = []
    start = time.time()
    for j in range(5):
        t = MyThread(j)   # 创建进程
        thread.append(t)

    for t in thread:
        t.start()       # 启动线程

    for t in thread:
        t.join()       # 主线程等待子线程

    end = time.time()
    print("运行时间：", end - start, "s")
