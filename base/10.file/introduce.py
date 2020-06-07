# open(file, mode='r', buffering=-1,encoding_=None, errors=None, closed=True,opener=None)
# file要打开文件的名字(路径)
# 返回一个对象，这个对象代表了当前打开的文件

file_name = 'a.txt'
file = open(file_name)
print(file)
# 读取文件
# read()可以接收一个size作为参数，该参数用来指定要读取的字符的数量
# 每一次读取都是从上次读取到的位置开始读取的
# 如果字符的数量小于size，则会读取剩余所有的
# 如果已经到了文件的最后了，则会返回''空串
content = file.read()
print(content)
file1 = open(file_name)
file2 = open(file_name)
print('readline', file1.readline(), end='')
print('readlines', file2.readlines())

with open(file_name, encoding='utf-8') as file_obj:
    # 在with语句中可以直接使用file_obj来作文件操作
    # 此时这个文件只能在with中使用，一旦with结束则文件自动close()
    print(file_obj.read())

for t in open(file_name):
    print('a', t)

# 关闭文件
file.close()
file1.close()
file2.close()
# 获取文件状态
print(file.closed)

# w表示可写的，如果文件不存在则会创建文件，如果存在则会截断文件，即删除原来文件中所有内容
# a表示追加，如果文件不存在也会创建文件,如果文件存在则会向文件中追加内容
# +为操作符增加功能
# r+:即可读又可写，但是文件不存在报错
# w+、a+:即可读又可写
# x:新建文件，如果文件不存在则创建，存在则报错
with open(file_name, 'w', encoding='utf-8') as file_writer:
    # write()写入内容，返回写入字符的长度
    file_writer.write('hello hello')

img_file = '/home/haijiwuya/Pictures/1.jpg'
# t 读取文本文件  b读取二进制文件
with open(img_file, 'rb') as img:
    # 读取二进制文件时，size是以字节为单位
    # content = img.read()
    # print(content)
    new_name = 'a.jpg'
    with open(new_name, 'wb') as new_img:
        buffer = 1024 * 100
        while True:
            content = img.read(buffer)
            if not content:
                print('执行完毕')
                break
            new_img.write(content)

with open('/home/haijiwuya/Pictures/2.jpg', 'rb') as new_img:
    print(new_img.read(100))
    # seek()可以修改当前读取的位置
    # seek()需要两个参数：第一个是要切换到的位置，第二个计算位置方式：0从头计算，默认值 1从当前位置计算 2 从最后位置开始计算
    new_img.seek(55)
    # tell()方法用来查看当前读取的位置
    print(new_img.tell())
