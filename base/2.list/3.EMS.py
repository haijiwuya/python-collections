"""
EMS(Employer Manager System员工管理系统)

"""
print('%s欢迎使用员工管理系统%s' % ("=" * 20, "=" * 20))
employers = [['张三', 12, '男', '北京市'], ['李四', 21, '男', '南京'],
            ['王二', 31, '男', '江苏常州'], ['赵武', 19, '男', '北京朝阳'],
            ['小芳', 18, '女', '河南郑州']]
titles = ['序号', '姓名', '年龄', '性别', '住址']

while True:
    print('请选择要执行的操作')
    print("\t1、查询员工")
    print("\t2、添加员工")
    print("\t3、删除员工")
    print("\t4、退出系统")
    operation = input("请选择:")
    if operation == '1':
        for title in titles:
            print(title, end='\t')
        print()
        # for employer in employers:
        for index in range(len(employers)):
            num = index + 1
            print(num, end='\t')
            employer = employers[index]
            for info in range(len(employer)):
                print(employer[info], end='\t')
            print()
    elif operation == '2':
        input_info = []
        input_name = input("请输入员工姓名:")
        input_info.append(input_name)
        input_age = input("请输入员工年龄:")
        input_info.append(input_age)
        input_sex = input("请输入员工性别:")
        input_info.append(input_age)
        input_address = input("请输入员工住址:")
        input_info.append(input_address)
        print("添加的员工信息为:")

        for title in titles:
            print(title, end='\t')
        print()
        print(1, end='\t')
        for index in range(len(input_info)):
            print(input_info[index], end='\t')
        print()
        flag = input("是否确认添加:Y确认  N取消")
        if flag == 'Y':
            employers.append([input_name, input_age, input_sex, input_address])
    elif operation == '3':
        num = int(input('请输入要删除的序号:'))
        if num < 0 or num > len(employers):
            print("序号输入有误")
            continue
        print("您要删除的数据为")
        for title in range(len(titles)):
            if title == 0:
                continue
            print(titles[title], end='\t')
        print()
        for employer in employers[num - 1]:
            print(employer, end='\t')
        print()
        flag = input("数据删除后无法恢复，是否确认：Y/N")
        if flag == 'Y':
            del employers[num - 1]
    elif operation == '4':
        input("谢谢使用!按Enter键退出")
        break
    else:
        print("选择有误，请重新选择")

