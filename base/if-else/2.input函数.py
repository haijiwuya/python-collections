"""
    input()函数
    该函数用来获取用户的输入
    input()调用后，程序会立即暂停，等待用户输入
    用户输入完内容以后，点击回车程序才会继续向下执行
    用户输入完成以后，其所输入的内容会以返回值的形式返回
    注意：input()函数的返回值是一个字符串
    input()函数中可以设置一个字符串作为参数，这个字符串将会作为提示文字显示
"""
a = input("请输入内容：")
print("您输入的内容是:", a)

username = input("请输入您的用户名:")
if username == 'admin':
    print("欢迎%s光临" % username)
