# class manager:
#     obj=None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.obj is None:
#             cls.obj=object.__new__(cls)
#             return cls.obj
#         else:
#             return cls.obj

class Manager(object):
    obj=None
    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj=object.__new__(cls)
            return cls.obj
        else:
            return cls.obj

class Manster(object):
    def __init__(self):
        super(Manster,self).__init__()
        self.instance=None
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance=super(Manster,self).__call__(*args, **kwargs)
        return self.instance
class boss:
    __metaclass__=Manster

m1=Manager()
m2=Manager()
print(id(m1))
print(id(m2))

b1=boss()
b2=boss()
print(id(b1))
print(id(b2))


class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instance


class MyClass3(object):
    __metaclass__ = Singleton2


one = MyClass3()
two = MyClass3()

print(id(one))
print(id(two))


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class MyClass4(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


one1 = MyClass4()
two1 = MyClass4()
print(id(one1))
print(id(two1))


def Best(cls,*args,**kwargs):
    instance={}
    def create():
        if cls not in instance:
            instance[cls]=cls(*args,**kwargs)
        return instance[cls]
    return create

@Best
class student:
    def get(self):
        print("GEt")

s1=student()
s2=student()
print(id(s1))
print(id(s2))


li=[11,222,11,22,134,555]
se=set(li)
print(se)
li=list(se)
print(li)




