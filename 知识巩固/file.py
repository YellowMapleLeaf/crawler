# def extendList(val,list=[]):
#     list.append(val)
#     return list
# list1=extendList(10)
# print(id(list1),list1)
#
# list2=extendList(123,[])
# print(id(list2),list2)
#
# list3=extendList('a')
# print(id(list3),list3)
#
#
# from copy import copy,deepcopy
# from pickle import dumps,loads
# a=[1,2,3]
# b=[a]*3
# print(b)
# c=copy(b)
# d=deepcopy(b)
# e=loads(dumps(b,4))
# print(a,id(a))
# b[1].append(100)
# print(b,id(b))
#
# c[1].append(200)
# print(c,id(c))
# print("*****")
# print(b,id(b))
# d[1].append(300)
# print(d,id(d))
#
# e[1].append(999)
# print(e,id(e))
#
#
#
# li=iter([1,2,3,4,5])
# print(next(li))
# print(next(li))
# print(next(li))
# print(next(li))
# print(next(li))
#
#
#
# from random import randrange
#
# def rand():
#     n = 1
#     while n<=30:
#         num=randrange(0,50)+1
#         yield num
#         n+=1
#
#
# func=rand()
# for i in range(30):
#     print(next(func))
#
# print("&&&&&&&&&&&&")




# class Test(object):
#     x = 123
#     def __init__(self):
#         self.y=456
#     def bar1(self):
#         print('Hello world')
#
#     @classmethod
#     def bar2(cls):
#         print('Bad world')
#
#     @staticmethod
#     def bar3():
#         print('=========')
#     def foo1(self):
#         print(self.x)
#         print(self.y)
#         self.bar1()
#         self.bar2()
#         self.bar3()
#     @classmethod
#     def foo2(cls):
#         print(cls.x)
#         # print(cls.y)
#         cls.bar1()
#         cls.bar2()
#         cls.bar3()
#
#     @staticmethod
#     def foo3(obj):
#         print(obj.x)
#         print(obj.y)
#         obj.bar1()
#         obj.bar2()
#         obj.bar3()
# t=Test()
# t.foo1()
# # t.foo2()
# Test.foo3(t)


# import time
# def timer(func):
#     def inner():
#         print("开始计时")
#         print(time.clock())
#         func()
#         print("结束计时")
#         print(time.clock())
#     return inner
#
# @timer
# def func():
#     time.sleep(3)
#     print("time out")
#
# func()


class Student:
    def __init__(self,name,age):
        self.mName=name
        self.__age=age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,ag):
        self.__age=ag

s1=Student('ssfd',19)

print(s1.age)
s1.age=222
print(s1.age)
