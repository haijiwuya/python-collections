"""
循环语句
    循环语句可以使指定的代码块重复指定的次数
    循环语句分成两种：while循环和for循环
while循环
语法：
    while 条件表达式:
        代码块
执行流程：
    while语句在执行时，会先对while后的条件表达式进行求值判断
    如果判断结果为True，则执行循环体(代码块)
    循环体执行完毕，继续对条件表达式进行求值判断，以此类推，
    直到判断结果为False，则循环终止
"""

while False:
    print("hello")

i = 0
while i < 10:
    print("hello", i)
    i += 1
j = 0
while j <= 5:
    print("5之内的数字", j)
    j += 1
else:
    print("5之外的数字", j)

"""
练习1：
求100以内所有的奇数之和
"""
a = 0
sum = 0
while a < 100:
    if a % 2 != 0:
        sum += a
    a += 1
print(sum)

"""
练习2：
求100以内所有7的倍数之和，以及个数
"""
i = 0
num = 0
count = 0
while i < 100:
    i += 1
    if i % 7 == 0:
        print(i)
        num += i
        count += 1
print("7的倍数之和为", num, "个数为", count)

"""
练习3：
水仙花数是指一个n位数(n>=3),它的每个位上的数字的n次幂之和等于它本身
例如：1 ** 3 + 5 ** 3 + 3 ** 3 = 153)
求1000以内所有的水仙花数
"""
i = 100
num = 0
while i < 1000:
    i += 1
    a = int(i / 1000)
    # num = (i - a * 1000) / 100
    num = i % 1000
    b = int(num / 100)
    num = num % 100
    c = int(num / 10)
    num = num % 10
    # print(a, b, c, num)
    if a ** 3 + b ** 3 + c ** 3 + num ** 3 == i:
        print("水仙花数", i)


"""
练习4：
获取用户输入的任意数，判断其是否是质数
判断是否是质数，只能被1和它自身整除的数就是质数
"""
num = int(input('输入一个任意的大于1的整数:'))
i = 2
flag = True
while i < num:
    if num % i == 0:
        flag = False
        break
    i += 1
if flag:
    print(num, "是质数")
else:
    print(num, '不是质数')














