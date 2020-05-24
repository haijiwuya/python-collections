class Person:
    # name定义为属性时，如果需要改值，需要手动一一改，比较麻烦，可以设置创建对象时，必须设置name属性
    name = '孙悟空'

    def __init__(self, name):
        self.name = name

    # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
    def say_hello(self):
        print('您好')


p1 = Person('猪八戒')
p2 = Person('孙悟空')

p1.say_hello()
p1.name = '猪八戒'
print(p1.name)
print(p2.name)


