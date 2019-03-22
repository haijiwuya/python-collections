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
print(max(set(a), key = a.count))

from collections import Counter
cnt = Counter(a)
print(cnt.most_common(3))

