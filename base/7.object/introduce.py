"""
对象
    对象是内存中专门用来存储数据的一块区域
    对象中可以存放各种数据
    对象由三部分组成：
        1.对象的标识(id)
        2.对象的类型(type)
        3.对象的值(value)
面向对象(oop)
    Python是一门面向对象的编程语言
    所谓的面向对象的语言，简单理解就是语言中的所有操作都是通过对象来进行的
    面向过程的编程的语言：面向过程指将程序逻辑分解为一个一个的步骤，通过对每个步骤的抽象，来完成程序
"""
a = int(10)  # 创建一个int类的实例
b = str('hello')  # 创建一个str类的实例

print(type(a))
print(type(b))


# 定义一个简单类，使用class关键字来定义类，使用类来创建对象和调用函数一样
class MyClass:
    pass


mc = MyClass()
mc_2 = MyClass()
mc_3 = MyClass()

print(mc, type(mc))

# isinstance()用来检查一个对象是否是一个类的实例
print(isinstance(mc, MyClass))
print(isinstance(mc_2, str))
