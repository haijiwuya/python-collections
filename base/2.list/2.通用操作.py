my_list = ['a', 'b', 'c', 'd', 'e', 'f']
# + 和 *
# + 可以将两个列表拼接为一个列表
my_list = my_list + ['g', 'h']
print(my_list)

# *可以将列表重复指定的次数
my_list = [1, 2, 3] * 5
print(my_list)

stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精']

# in 和 not in
# in用来检查指定元素是否存在于列表中
# not in用来检查指定元素是否不存在列表中
print('猪八戒' in stus)
print('牛魔王' not in stus)

# min()获取列表中的最小值
print(min(stus))
# max()获取列表中的最大值
print(max(stus))

# 两个方法index() count()
print(stus.index("唐僧"))
print(stus.count("唐僧"))

# 修改列表
# 通过索引来修改元素
stus[0] = "sunwukong"
print(stus)
# 通过del删除元素
del stus[0]
print(stus)
# 通过切片来修改列表
stus[0: 2] = {'a', "b"}
print(stus)     # ['a', 'b', '唐僧', '蜘蛛精']
stus[0: 2] = {'a', "b", "c"}
print(stus)     # ['a', 'b', 'c', '唐僧', '蜘蛛精']
# 向索引为0的位置插入元素
stus[0: 0] = "a"
print(stus)
# 当设置了步长时，序列中元素的个数必须和切片中元素的个数一致
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精']
stus[:: 2] = ['牛魔王', '红孩儿', '老虎精']
print(stus)

# 列表的方法
test_list = ['a', 'b', 'c', 'd']
# append()  向列表的最后添加一个元素
test_list.append('e')
print(test_list)

# insert() 向列表指定位置添加一个元素
test_list.insert(3, 'f')
print(test_list)

# extend() 使用新的序列扩展当前序列
test_list.extend(['g', 'h'])
print(test_list)

# clear() 清空序列
# test_list.clear()
print(test_list)

# pop() 根据索引删除并返回被删除的元素
new_list = test_list.pop(2)
print(test_list)
print(new_list)

# remove() 删除指定元素，如果指定元素有多个，只会删除第一个
test_list.remove('f')
print(test_list)

# reverse() 反转列表
test_list.reverse()
print(test_list)

# sort() 排序列表中元素
test_list.sort()    # 升序
test_list.sort(reverse=True)    # 降序
print(test_list)

# 遍历列表
i = 0
while i < len(test_list):
    print(test_list[i])
    i += 1

for a in test_list:
    print(a)
