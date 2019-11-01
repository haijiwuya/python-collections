"""
    练习1：
        编写一个程序，获取用户输入的整数。然后通过程序显示这个数是奇数还是偶数
"""
a = int(input("请输入数字:"))
if a % 2 == 0:
    print("您输入的是偶数", a)
else:
    print("您输入的是奇数", a)

"""
练习2：
    编写一个程序，检查任意一个年份是否闰年
    如果一个年份可以被4整除不能被100整除，或者可以被400整除，这个年份就是闰年
"""
year = int(input('请输入年份:'))
if year <= 0:
    print('请输入正确的年份')
elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("闰年")
else:
    print("平年")

"""
练习3：
    我家的狗5岁了，5岁的狗相当于多大年龄的人呢？
    其实非常简单，狗的前两年每一年相当于人的10.5岁，然后每增加一年就增加四岁
"""
dogAge = int(input('请输入狗的年龄:'))
if dogAge >= 2:
    dogAge = 2 * 10.5 + (dogAge - 2) * 4
elif 0 < dogAge < 2:
    dogAge *= 10.5
else:
    print('输的值不能小于0')
print(int(dogAge))

"""
练习4：
    从键盘输入小明的期末成绩
        当成绩为100时，奖励一辆bmw
        当成绩为80-99时，奖励一台iphone
        当成绩为60-80时，奖励一本参考书
"""
grade = int(input('请输入成绩:'))
if grade < 0:
    print("请输入正确的成绩")
elif grade == 100:
    print("奖励一辆BMW")
elif 80 <= grade <= 99:
    print("奖励一台iphone")
elif 60 <= grade < 80:
    print("奖励一本参考书")
else:
    print("没有奖励")

"""
练习5：
    大家都知道，男大当婚女大当嫁，那么女方家长要嫁女儿，当然要提出一定的条件：
        高：180cm以上；富：1000万以上；帅：500以上；
        如果这三个条件同时满足，则：‘我一定要嫁给他’
        如果三个条件有为真的情况，则：‘嫁吧，比上不足，比下有余’
        如果三个条件都不满足，则：‘不嫁’
"""
height = int(input("请输入您的身高"))
rich = int(input("请输入您的财产，单位为万"))
handsome = int(input("请输入您的帅气值"))
if height <= 0 or rich <= 0 or handsome <= 0:
    print("别开玩笑了，请输入正确的值")
elif height > 180 and rich > 1000 and handsome > 500:
    print("我一定要嫁给他")
elif height > 180 or rich > 1000 or handsome > 500:
    print("嫁吧，比上不足，比下有余")
else:
    print("不嫁")
