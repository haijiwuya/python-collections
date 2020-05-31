"""
开箱即用：为了实现开箱即用的思想，python中提供了一个模块的标准库
"""
# sys模块，提供了一些变量和函数，是我们可以获取到Python解析器的信息
import sys

# pprint 提供了一个方法pprint() 用来对打印的数据作简单的格式化
import pprint

# os模块提供了对操作系统的访问
import os

# 返回一个列表，列表中保存了当前命令的所有参数
print(sys.argv)

# 返回一个字典，获取当前程序中引入的模块
print(sys.modules)
pprint.pprint(sys.modules)

# 返回一个列表，列表中保存的是模块的搜索路径
print(sys.path)

# 获取当前Python运行的平台，也即操作系统信息
print(sys.platform)

# 退出程序
# print(sys.exit())
print('hello')

print(os)
# 获取系统的环境变量
pprint.pprint(os.environ)
pprint.pprint(os.environ['PATH'])

# 用来执行操作系统的命令
os.system('ls')
