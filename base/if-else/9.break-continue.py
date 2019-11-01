"""
break
break可以用来立即退出循环语句(包括else)

continue
continue可以用来跳出当次循环

pass
pass是用来在判断或循环语句中占位的
"""
i = 0
while i < 5:
    if i == 2:
        break
    print(i)
    i += 1

j = 0
while j <= 4:
    j += 1
    if j == 3:
        continue
    print(j)

i = 0
if i < 5:
    pass
