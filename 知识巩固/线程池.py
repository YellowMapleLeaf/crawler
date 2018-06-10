import time
import threadpool

def long_op(n):
    print('%d\n' % n)
    time.sleep(2)


#创建3个线程的线程池
pool=threadpool.ThreadPool(3)
#创建任务
tasks=threadpool.makeRequests(long_op,[1,2,3,4,5,6,7,8,9,0])
#执行任务
[pool.putRequest(task) for task in tasks]

#等待线程任务处理完
pool.wait()
