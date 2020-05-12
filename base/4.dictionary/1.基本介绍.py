"""
字典(dict)
字典属于一种新的数据结构，称为映射(mapping)
列表存储数据的性能很好，但是查询数据的性能很差
在字典中每一个元素都有一个唯一的名字，通过这个唯一的名字可以快速的查找到指定的元素
在查询元素时，字典的效率是非常快的
"""
# 常用创建方式
d = {"name": "孙悟空", "age": 18, "sex": "男"}
print(d["name"])
# 使用dict()函数来创建字典
b = dict(name='孙悟空', age=18, sex="男")
print(b["name"])
# 也可以将一个含有双值序列的序列转换为字典
d = dict([('name', '孙悟空'), ('age', 18)])
print(d, type(d), d['age'])

# len()获取字典中键值对的个数
print(len(d))
# in检查字典是否包含指定键
# not in检查字典中是否不包含指定的键
print('hello' in d)

# 获取字典中的值，根据键来获取
# 如果键不存在，会抛出异常KeyError
print(d['age'])

# get(key[, default])来获取值，如果获取的键在字典中不存在，会返回None
# 如果键不存在，并且指定了默认值，就会返回默认值
print(d.get('hello'))  # None
print(d.get('hello', '默认值'))  # 默认值

# 修改字典
d['name'] = 'sunwukong'
print(d)
# 如果键不存在则插入数据
d['address'] = '花果山'
print(d)

# setDefault(key[,default])，如果key在字典中，返回它的值，如果不存在则插入
d.setdefault("name", "猪八戒")
print(d)
d.setdefault("sex", '男')
print(d)

# update([other]):将其他的字典中的key-value添加到当前字典中
d = {"a": 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5}
d.update(d2)
print(d)

# 删除，可以使用del来删除字典中的key-value
del d['a']
print(d)
del d['b']
print(d)

# popitem() 随机删除字典中的一个键值对，一般都会删除最后一个键值对,并且删除之后将删除的key-value作为返回值以元组的形式返回
# popitem()删除一个空字典会抛出异常
result = d.popitem()
print(d)
print(result)

# pop(key[, default])
# 根据key删除字典中的key-value，将被删除的value返回
# 如果被删除的key不存在，则抛出异常，可以指定默认值再删除
result = d.pop('d')
d.pop('f', '这是默认值')
print(result, d)

# clear()用来清空字典
d.clear()
print(d)

# copy() 用来对字典进行浅复制,复制以后的对象和原对象是独立的，修改一个不会影响另一个
# 浅复制会简单复制对象内部的值，如果值是一个可变对象，这个可变对象不会被复制
d = {"a": 1, 'b': 2, 'c': 3}
print(d.copy())

d = {'a': {'name': '孙悟空', 'age': 18}, 'b': 2, 'c': 3}
d2 = d.copy()
d2['a']['name'] = '猪八戒'
print('d=', d, id(d))
print('d2=', d2, id(d2))

# 遍历字典
d = {'a': {'name': '孙悟空', 'age': 18}, 'b': 2, 'c': 3}
for k in d.keys():
    print(k)
    print(d[k])
print(d.values())
print(d.items())
