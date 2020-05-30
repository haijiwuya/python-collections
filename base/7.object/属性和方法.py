class A(object):
    # 类属性，直接在类中定义的属性是类属性
    # 类属性可以通过类或类的实例访问到
    # 类属性只能通过类对象来修改，无法通过实例对象修改
    count = 0

    def __init__(self):
        # 实例属性，通过实例对象添加的属性属于实例属性
        # 实例属性只能通过实例对象来访问和添加，类对象无法访问修改
        self.name = '孙悟空'

    # 实例方法：在类中定义，以self为第一个参数的反法都是实例方法
    # 实例方法调用时，Python会将调用对象作为self传入
    # 实例方法可以通过实例和类去调用
    # 当通过实例调用时，会自动将当前对象作为self传入
    # 当通过类调用时，不会自动传递self，此时需要手动传递
    def test(self):
        print('这是test方法....', self)

    # 类方法：在类内部使用@classmethod修饰的方法
    # 类方法的第一个参数是cls，也会被自动传递
    @classmethod
    def test2(cls):
        print('这是test2方法，它是一个类方法')
        print(cls.count)

    # 静态方法:在类中使用@staticmethod来修饰的方法属于静态方法
    # 静态方法不需要指定任何的默认参数，静态方法可以通过类实例去调用
    @staticmethod
    def test3():
        print('静态方法test3执行....')


a = A()
a.count = 10
A.count = 100
print(A.count)
print(a.count)
# print(A.name)
print(a.name)

print(a.test())
print(A.test(self=a))
A.test2()
a.test3()
A.test3()
