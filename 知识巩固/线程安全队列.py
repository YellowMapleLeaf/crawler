import queue
import threading
def printf(n):
    print(n)

#FIFO
q=queue.Queue()
for i in range(5):
    q.put(i)

while not q.empty():
    printf(q.get())

#FILO
q=queue.LifoQueue()
for i in range(5):
    q.put(i)

while not q.empty():
    printf(q.get())


#优先级对列
class task:
    def __init__(self,priority,description):
        self.priority=priority
        self.description=description

    def __lt__(self, other):
        return self.priority<other.priority

#创建优先级对列
q=queue.PriorityQueue()
q.put(task(1,"the most importnat"))
q.put(task(10,"importnat"))
q.put(task(100,"normal importnat"))

def join():
    while not q.empty():
        print(q.get().description)

t1=threading.Thread(target=join)
t2=threading.Thread(target=join)

t1.start()
t2.start()
t1.join()
t2.join()


