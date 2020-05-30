class Animal:
    def __init__(self, name):
        self._name = name

    def run(self):
        print('动物会跑...')

    def sleep(self):
        print('动物睡觉....')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# 父类中的所有方法都会被子类继承，包括特殊方法
class Dog(Animal):

    def __init__(self, name, age):
        # 可以直接调用父类的__init__来初始化父类中定义的属性
        # Animal.__init__(self, name)
        # super()可以用来获取当前类的父类,并且不需要传递self
        super().__init__(name)
        self._age = age

    def bark(self):
        print('汪汪汪....')

    def run(self):
        print('狗跑....')


d = Dog('旺财', 18)
d.name = '小黑'
print(d.name)
# 类名.__bases__这个属性用来获取当前类的所有父类
print(Dog.__bases__)