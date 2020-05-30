"""
封装是面向对象的三大特性之一
封装是隐藏对象中一些不希望被外部所访问到的属性或方法
双下划线开头的属性，是对象的隐藏属性，隐藏属性只能在类的内部访问
"""


class Animal(object):
    def run(self):
        print('动物跑')

    def sleep(self):
        print('动物睡觉')


class Dog(Animal):

    def __init__(self, name):
        self.__name = name

    # property装饰器，用来将一个get方法，转换为对象的属性
    # 添加为property装饰器以后，就可以像调用属性一样使用get方法
    @property
    def get_name(self):
        return self.__name

    # setter方法的装饰器：@属性名：setter
    @get_name.setter
    def set_name(self, name):
        self.__name = name

    def run(self):
        print('狗跑...')


p = Dog('哈士奇')

# print(p.get_name())
p.set_name = '二狗'
print(p.get_name)

print(isinstance(Dog, object))
print(issubclass(Animal, Dog))
print(issubclass(Animal, object))
# 如果在子类中有和父类同名的方法，则通过子类实例去调用方法时，会调用子类的方法而不是父类的方法
# 这称为方法的重写(override)
# 当我们调用一个对象的方法时，会优先去当前对象中寻找该方法，如果没有则去当前类的父类去寻找，如果父类中也没有，
# 则去父类的父类寻找，直到找到object，如果依然没有找到，则报错
p.run()
