"""
    集合和列表非常相似
    不同点：
        1、集合中只能存储不可变对象
        2、集合中存储的对象是无序的
        3、集合中不能出现重复的元素
"""
s = {1, 2, 3, 4}
print(s, type(s))
# 空集合只能通过set()函数来创建
s = set()
print(s, type(s))
# s = set([1, 2, 3, 4, 5])
s = {1, 2, 3, 4, 5}
print(s, type(s))

# 使用set()将字典转换为集合只包含集合中的键
# s = set({'a': 1, 'b': 2, 'c': 3})
s = {'a': 1, 'b': 2, 'c': 3}
print(s, type(s))

# 使用in 和not in来检查集合中的元素
s = {'a', 'b', 1, 2, 3, 1}
print('c' in s)
print('a' in s)

# 使用len()来获取集合中元素的数量
print(len(s))

# add()向集合中添加元素
s.add(10)
s.add(30)
print(s)

# update()将一个集合中的元素添加到当前集合中
s2 = set('hello')
s.update(s2)
print(s)

# pop()随机删除一个集合中的元素,并返回删除的元素
s.pop()
print(s)

# remove()删除集合中的指定元素
s.remove(30)
print(s)

# clear()清空集合
s.clear()
print(s)

# copy()对集合进行浅复制

s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
# &交集运算
result = s & s2
print(result)

# |并集运算
result = s | s2
print(result)

# -差集
result = s - s2
print(result)

# ^异或集
result = s ^ s2
print(result)

# <=检查一个集合是否另一个集合的子集,如果两个集合元素一样，也算一个集合是另一个集合的子集
result = s <= s2
print(result)

# < 检查一个集合是否是另一个集合的真子集(两个集合元素不相同)
s = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print(s < s2)

# >= 检查一个集合是否是另一个集合的超集
# > 检查一个集合是否是另一个集合的真超集
