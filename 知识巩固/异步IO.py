# import asyncio
#
#
# @asyncio.coroutine
# def wget(host):
#     connect=asyncio.open_connection(host,80)
#     reader,writer=yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     print(header)
#     writer.write(header.encode("utf-8"))
#     yield from writer.drain()
#     while True:
#         data=yield from reader.readline()
#         if data==b"\r\n":
#             break
#         print('%s header > %s' % (host, data.decode('utf-8').rstrip()))
#     writer.close()
#
#
# #获取事件循环
# loop=asyncio.get_event_loop()
#
# #创建任务
# tasks=[wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
# #等待结束
# loop.run_until_complete(asyncio.wait(tasks))
# #关闭
# loop.close()

"""
www.sina.com', 'www.sohu.com', 'www.163.com'
"""

import asyncio
@asyncio.coroutine
def wget(host):
    connect=asyncio.open_connection(host,80)
    reader,writer=yield from connect
    header="GET/HTTP/1.0\r\nHost: %s\r\n\r\n" % host
    print(header)
    writer.write(header.encode("utf-8"))
    while True:
        data=yield from reader.readline()
        if data==b'\r\n':
            break
        print("host:%s--->data:%s"%(host,data.decode("utf-8")))

loop=asyncio.get_event_loop()
tasks=[wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

