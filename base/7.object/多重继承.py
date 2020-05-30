class A(object):
    def test(self):
        print('AAA')


class B(object):
    
    def test(self):
        print('BBB')

    def test2(self):
        print('BBB')


# python中是支持多继承的，可以在类名的()里添加多个类来实现多继承
# 如果多个父类中有同名的方法，则从第一个父类依次向后查找，直到直到，找不到则报错
class C(A, B):
    pass


print(C.__bases__)
c = C()
c.test()
c.test2()