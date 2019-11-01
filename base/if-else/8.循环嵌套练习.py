from time import time
"""
打印99乘法表
"""
a = 1
while a <= 9:
    b = 1
    while b <= a:
        # print("%s * %s = %s   " % (b, a, a * b), end="")
        print(f"{b} * {a} = {b*a}  ", end="")
        b += 1
    print()
    a += 1

"""
求100以内所有的质数
"""
a = time()
i = 2
while i <= 100:
    flag = True
    j = 2
    while j < i:
        if i % j == 0:
            flag = False
        j += 1
    if flag:
        print("%s 是质数" % i)
    else:
        print("%s 不是质数" % i)

    i += 1
b = time()


"""
优化上面代码
"""
start = time()
i = 2
while i <= 100:
    flag = True
    j = 2
    while j < i:
        if i % j == 0:
            flag = False
            break
        j += 1
    if flag:
        print("%s 是质数" % i)
    else:
        print("%s 不是质数" % i)

    i += 1
stop = time()
print(b - a)
print(stop - start)

"""
第二次优化
"""
begin = time()
i = 2
while i <= 100:
    flag = True
    j = 2
    while j <= i ** 0.5:
        if i % j == 0:
            flag = False
            break
        j += 1
    if flag:
        print("%s 是质数" % i)
    else:
        print("%s 不是质数" % i)

    i += 1
end = time()
print(b - a)
print(stop - start)
print(end - begin)
