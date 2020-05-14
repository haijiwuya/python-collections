"""
函数也是一个对象
对象是内存中专门用来存储数据的一块区域
函数可以用来保存一些可执行的代码，并且可以在需要时，对这些语句进行多次的调用
创建函数：
    def 函数名([形参1，形参2，形参3...]):
        代码块
    函数名称必须要符合标识符的规范：包含数字、字母、下划线，但不能以数字开头

函数中保存的代码不会立即执行，需要调用
"""


def fn():
    print("这是我第一个函数")


print(fn)
print(type(fn))
fn()


def add(a, b):
    print(a, "+", b, "=", a + b)


add(23, 5)

"""
实参的传递方式:
    1.位置参数
    位置参数就是将对应位置的实参复制给对应位置的形参
    2.关键字参数
    关键字参数可以不按照形参定义的顺序去传递，而直接根据参数名去传递参数
    3.混合使用关键字和位置参数，必须将位置参数写到前面
"""
add(a=12, b=13)
add(21, b=30)


# 可变参数不是必须写在最后，但是，带*的参数后的所有参数，必须以关键字的形式传递
# 如果在形参的开头直接写一个*，则要求所有的参数必须以关键字形式传递
def fn2(a, *b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


def fn3(*, a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fn2(1, 2, 3, 4, c=5)
fn3(a=3, b=4, c=5)


# **形参可以接收其他的关键字参数
# **形参只能有一个，并且必须写在所有参数的最后
def fn4(**a):
    print('a=', a, type(a))


def fn5(b, c, **a):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fn4(b=1, d=2, c=3)
fn5(a=1, b=2, c=3, d=4, e=5)
