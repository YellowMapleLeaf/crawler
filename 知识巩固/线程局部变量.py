import time
import threading

#创建线程局部变量
thread_local=threading.local()

def printf():
    print(threading.current_thread().name,thread_local.name)


def threadDeal(name):
    thread_local.name=name
    printf()

t1=threading.Thread(target=threadDeal,args=('TOM',))
t2=threading.Thread(target=threadDeal,args=('JAVA',))

t1.start()
t2.start()
t1.join()
t2.join()











