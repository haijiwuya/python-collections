"""
元组是不可变的序列
它的操作方式基本上和列表是一致的
一般当我们希望数据不改变时，就使用元组
"""

# 创建元组，使用()
my_tuple = ()
print(type(my_tuple))
my_tuple = (1, 2, 3)
print(my_tuple)
print(my_tuple[1])

# 当元组不是空元组时，可以省略括号
my_tuple = 10, 20, 30, 40
print(my_tuple)

# 元组解包(解构),就是将元组当中每一个元素都赋值给一个变量
a, b, *c = my_tuple
print(f"a = {a}, b = {b}, c = {c}")

a, b = b, a
print(a, b)