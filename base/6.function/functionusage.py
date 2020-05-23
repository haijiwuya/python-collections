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


# 参数的解包
def fn6(a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


# 创建一个元组
t = (10, 20, 30)

# 传递实参时，也可以在序列类型的参数前添加星号
# 这里要求序列中元素的个数必须和形参的个数一致
fn6(*t)

# 创建一个字典,通过**来对一个字典进行解包操作
d = {'a': 100, 'b': 200, 'c': 300}
fn6(**d)


# 返回值，函数执行以后返回的结果。通过return来指定函数的返回值
# 如果仅仅写一个return或者不写return，则相当于return None
# 在函数体内，return一旦执行，后续的代码块都不会被执行
def sum(*nums):
    total = 0
    for n in nums:
        total += n
    print(total)
    return total


result = sum(123, 456, 789)
print(result)


def fn():
    for i in range(5):
        if i == 3:
            # break用来退出当前循环
            # break
            # continue用来跳过当次循环
            continue
        print(i)


fn()
# print(fn)打印fn函数对象，print(fn())调用函数，打印函数的返回值
print(fn)
print(fn())


# 文档字符串:在定义函数时，可以在函数内部编写文档字符串，文档字符串就是函数的说明
# 当我们编写了文档字符串时，都可以通过help()函数来查看函数的说明
# 文档字符串非常简单，其实直接在函数的第一行写一个字符串就是文档字符串
def fn(a: int, b: bool, c: str = 'hello') -> int:
    """
    这是一个文档字符串的示例
    函数的作用：.......
    函数的参数：
        a，作用，类型，默认值......
        b，作用，类型，默认值......
        c，作用，类型，默认值......
    ...
    :return: int
    """


help(fn)

# 命名空间(namespace)：变量存储的位置，每一个变量都需要存储到指定的命名空间当中
# 全局命名空间，用来保存局部变量；函数命名空间用来保存函数中的变量

# locals()用来获取当前作用域的命名空间
# 如果在全局作用域中调用locals()则获取全局命名空间，如果在函数中调用locals()则获取函数中的命名空间
# locals()返回的就是一个字典
scope = locals()
print(scope)

# 向scope中添加一个key-alue,相当于在全局中创建了一个变量
scope['c'] = 100
print(c)

# globals()函数可以在任意位置获取全局命名空间
print(globals()['c'])


# 递归
def factorial(n):
    """
    该函数用来求任意数的阶乘
    :param n:
    :return:
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(2))


# 创建一个函数求任意字符的幂
def power(num, times):
    if times == 1:
        return num
    return num * power(num, times - 1)


print(pow(10, 2))


# 判断任意字符是否是回文字符串
def isHuiwen(str):
    length = len(str)
    if length == 1:
        return False
    elif length % 2 == 0:
        return False
    chara = str[0: length // 2]
    charb = str[length // 2 + 1:]
    if list(reversed(chara)) == list(charb):
        return True


print(isHuiwen('abcb'))

"""
在python中，函数是一等对象
    一等对象特点：
        1、对象是在运行时创建的
        2、能赋值给变量或作为数据结构中的元素
        3、能作为参数传递
        4、能作为返回值返回
    高阶函数：
        1、接收一个或多个函数作为参数
        2、将函数作为返回值返回
"""

"""
lambda函数表达式专门用来创建一些简单的函数
lambda 参数列表：返回值
"""

lambda a, b: a + b
# 调用
print((lambda a, b: a + b)(10, 20))

# 也可将匿名函数赋值给一个变量
count = lambda a, b: a + b
print(count(10, 30))

# map()函数可以对可迭代对象中的所有元素做指定的操作
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = map(lambda i: i + 1, l)
print(list(r))

# sort()用来对列表中的元素进行排序
# 在sort()中可以接受一个关键字参数
# 该关键字可以以函数作为关键字，每次都会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小
chars = ['aa', 'cc', 'bb', 'ddd', 'oo']
chars.sort()
print(chars)

# sorted()和sort()的用法基本一致，但是sorted()可以对任意的队列进行排序
# 并且不会影响原来的对象，而是返回一个新对象

l = [2, 5, '1', 3, '6', '4']
print(sorted(l, key=int))


# 将函数作为返回值返回
# 这种高阶函数也称为闭包，通过闭包可以创建一些只有当前函数能访问的变量，可以将一些私有的数据藏到闭包中
def fn():
    # 函数内部再定义一个函数
    def inner():
        print('我是fn2')

    # 将内部函数inner作为返回值返回
    return inner


print(fn())

# r是一个函数，是调用fn()后返回i的函数 这个函数在fn()内部定义，并不是全局函数，所以这个函数总是能访问到fn()函数内的变量
r = fn()


def make_average():
    nums = []

    def doaverage(n):
        nums.append(n)
        return sum(*nums) / len(nums)

    return doaverage


average = make_average()

print(average(10))
print(average(20))
print(average(10))
