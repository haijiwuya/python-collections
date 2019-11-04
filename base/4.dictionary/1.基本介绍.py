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
