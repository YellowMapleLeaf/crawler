import random


def producter(c):
    c.send(None)
    for i in range(5):
        print("生产者生产数据~")
        r=c.send(str(i))
        print("消费者消耗了%s"%r)

def customer():
    data=""
    while True:
        n=yield data
        if n:
            print("生产者消费了%s"%n)
        else:
            break
        data="200"
c=customer()
producter(c)
























