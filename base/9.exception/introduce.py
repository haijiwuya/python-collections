"""
异常：程序在运行过程当中，不可避免的会出现一些错误，这些错误，称其为异常。
程序在运行过程中，一旦出现异常会导致程序立即终止，异常以后的代码不会被执行
"""
try:
    print(10 / 1)
except NameError as e:
    print('参数不存在', e, type(e))
except ZeroDivisionError as e:
    print('出错了', e, type(e))
else:
    print('程序执行完成')
finally:
    print('方法调用完成')


# raise抛出异常，raise语句后需要跟一个异常类
def add(a, b):
    if a < 0 or b < 0:
        # raise Exception
        raise Exception('参数不能小于0')
    r = a + b
    return r


print(add(123, -1))
