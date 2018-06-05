import threading
import requests

def display_info(code):
    url=r'http://hq.sinajs.cn/list=' + code
    response=requests.get(url).text
    print(response)

def single_thread(codes):
    for code in codes:
        code = code.strip()
        display_info(code)

def thread_deal(tasks):
    threads=[threading.Thread(target=single_thread,args=(codes,)) for codes in tasks]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__=="__main__":
    codes=['sh600001', 'sh600002', 'sh600003', 'sh600004', 'sh600005', 'sh600006']
    #线程的数量
    threads_len=4
    #每一个线程需要处理的数据量
    num=int(len(codes)/threads_len)
    #每一个线程处理的任务
    tasks=[]
    for i in range(3):
        task=codes[i*num:(i+1)*num]
        tasks.append(task)
        tasks.append(codes[(threads_len-1)*num:])
    # print(threads)
    thread_deal(tasks)