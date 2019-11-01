"""
在控制台中打印如下图形
*****
*****
*****
*****
创建一个循环来控制图形的高度
"""
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print("*", end='')
        j += 1
    print()
    i += 1
    
a = 1
while a <= 5:
    print("*" * a)
    a += 1
