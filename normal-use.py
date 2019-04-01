"""变量值交换 pythonic way of value swapping"""
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)

# 把list的所有元素拼接成一个字符串
'''
    巧妙运用了字符串的join()方法
    连接符可以是任意字符串
    被join的可以是任意的可迭代对象
    如：
        列表、字典、集合、元组等
'''
a = {'Python', 'is', 'awesome'}
print(" ".join(a))

# 找出list中出现频率最高的元素
a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(max(set(a), key=a.count))

from collections import Counter
cnt = Counter(a)
print(cnt.most_common(3))

# 判断两个字符串是否相等
print(Counter("123") == Counter("123"))
print(Counter("124") == Counter("123"))

# 反转字符串
'''reversing string with special case of slice step param'''
a = 'abcdefghijklmnopqrstuvwxyz'
print(a[::-1])
'''iterating over string contents in reverse efficiently'''
for char in reversed(a):
    print(char)

'''reversing an integer through type conversion and slicing'''
num = 123456789
print(int(str(num)[::-1]))

# 反转列表 reversing list with special case of slice step param
a = [5, 4, 3, 2, 1]
print(a[::-1])

'''iterating over list contents in reverse efficiently'''
for ele in reversed(a):
    print(ele)

# 转置2D阵列 transpose 2d array[[a, b], [c, d], [e, f]] --> [[a, c, e], [b, d, f]]
original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*original)
print(list([transposed]))

'''chained comparison with all kind of operators'''
b = 6
print(4 < b < 7)
print(1 == b < 20)

# 格式函数调用 calling different functions with same arguments based on condition
def product (x, y):
    return x * y
def add(x, y):
    return x + y
b = True
print((product if b else add)(5, 7))

#列表复制
'''a fast way to make a shallow copy of a list'''
b = a
b[0] = 10
'''both a and b will be [10, 2, 3, 4, 5]'''
b = a[:]
b[0] = 10
'''only b will change to [10, 2, 3, 4, 5]'''

'''copy list by typecasting method'''
a = [1, 2, 3, 4, 5]
print(list(a))

'''using the list.copy() method'''
a = [1, 2, 3, 4, 5]
print(a.copy())

'''copy nested lists using copy.deepcopy'''
from copy import deepcopy
l = [[1, 2], [3, 4]]
l2 = deepcopy(l)
print(l2)

# 字典的get方法 returning None or default value, when key is not in dict
d = {'a': 1, 'b': 2}
print(d.get('c', 3))

# 按值排序字典
'''sort a dictionary by its values with the built-in sorted() function and a 'key' argument'''
d = {'apple': 10, 'oragnge': 20, 'banana': 5, 'rotten tomato': 1}
print(sorted(d.items(), key=lambda x: x[1]))

'''sort usring operator, itemgetter as the sort key instead of a lambda'''
from operator import itemgetter
print(sorted(d.items(), key=itemgetter(1)))

'''sort dict keys by value'''
print(sorted(d, key=d.get))

'''else gets called when for loop does not rearch break statement'''
a = [1, 2, 3, 4, 5]
for el in a:
    if el == 0:
        break
    else:
        print('did not break out of for loop')

# 把列表用符号拼接成字符串
'''converts list to comma separted string'''
items = ['foo', 'bar', 'xyz']
print(','.join(items))

'''list of numbers to comma separted'''
numbers = [2, 3, 5, 10]
print(','.join(map(str, numbers)))
'''list of mix data'''
data = [2, 'hello', 3, 3.4]
print(','.join(map(str, data)))

# 合并字典
'''merge dict's'''
d1 = {'a': 1}
d2 = {'b': 2}
print({**d1, **d2})
print(dict(d1.items() | d2.items()))

'''find index of min/max element'''
list = [40, 10, 20, 30]
def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)

def maxIndex(lst):
    return max(range(len(lst)), key=lst.__getitem__)
print(minIndex(list))
print(maxIndex(list))

'''remove duplicate items from list
    does not preserve the original list order
'''
items = [2, 2, 3, 3, 1]
newitems2 = list(set(items))
print(newitems2)

'''reomve dups and keep order'''
from collections import OrderedDict
items = ['foo', 'bar', 'bar', 'foo']
print(list(OrderedDict.fromkeys(items).keys()))
