"""
模块(module)
模块化，将一个完整的程序分解为一个一个小的模块，通过模块组合，来搭建出一个完整的程序
在python里一个python文件就是一个模块
在一个模块中引入外部模块
1.import 模块名(python文件的名字，不需要扩展名)
    可以引入同一个模块多次，但是模块的实例只会创建一次
    import可以在程序的任意位置调用，但是一般情况下，import语句统一写在程序的开头
    在每一个模块内部都有一个__name__属性，通过这个属性可以获取到模块的名字
    __name__属性值为__main__的模块是主模块，一个程序中只有一个主模块
    主模块就是直接通过python执行的模块
2.import 模块名 as 模块别名


包packae，也是一个模块
当模块中代码过多时，或者一个模块需要被分解为多个模块时，就需要用到包
普通的模块就是一个python文件，而包是一个文件
包中必须要有一个__init__.py文件
__pycache__是模块的缓存文件
python在执行前，需要被解析器先转换为机器码，然后再执行
为了提高程序运行的性能，python会在编译过一次后，将代码保存到一个缓存文件中，
这样下次再加载这个模块(包)时，就可以不再编译而是直接加载缓存中编译好的代码即可
"""
import test_module as test
import base
from base import ab

# print(test_module)
print(test)
# 从不同的python文件执行__name__当前文件打印出的为__main__
print(__name__)

print(base.a)
print(base.b)
print(base.test())
print(ab.test())