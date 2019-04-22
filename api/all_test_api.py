# coding:utf-8
from my_dispatcher import api_add
a = 0


@api_add
def my_method(*args, **kwargs):
    global a
    a += 1
    print(a)
    return a


