import pandas as pd
import csv
# 定义一个函数，显示可以使用的功能列表给用户
def showInfo():
    print("-" * 30)
    print("     学生疫情上报系统    ")
    print(" 1.添加学生的信息")
    print(" 2.删除学生的信息")
    print(" 3.修改学生的信息")
    print(" 4.查询学生的信息")
    print(" 5.遍历所有学生的信息")
    print(" 6.存储学生信息")
    print(" 7.退出系统")
    print('-' * 30)
# 定义一个列表，用来存储多个学生的信息
students = []
while True:
    showInfo()
    # 提示用户选择功能
    key = int(input("请选择功能（序号）："))
    # 根据用户选择，完成相应功能
    if key == 1:
        print("您选择了添加学生信息功能")
        name = input("请输入学生姓名：")
        stuId = input("请输入学生学号(学号不可重复)：")
        college = input("请输入学生学院:")
        address = input("请输入学生地址：")
        time = input("请输入填报时间：")
        healthy = input("请输入健康状况：")
        # 验证学号是否唯一
        i = 0
        leap = 0
        for temp in students:
            if temp['id'] == stuId:
                leap = 1
                break
            else:
                i = i + 1
        if leap == 1:
            print("输入学生学号重复，添加失败！")
            break
        else:
            # 定义一个字典，存放单个学生信息
            stuInfo = {}
            stuInfo['name'] = name
            stuInfo['id'] = stuId
            stuInfo['college'] = college
            stuInfo['address'] = address
            stuInfo['time'] = time
            stuInfo['healthy'] = healthy
            # 单个学生信息放入列表
            students.append(stuInfo)
            print("添加成功！")
    elif key == 2:
        print("您选择了删除学生功能")
        delId = input("请输入要删除的学生学号:")
        # i记录要删除的下标，leap为标志位，如果找到leap=1，否则为0
        i = 0
        leap = 0
        for temp in students:
            if temp['id'] == delId:
                leap = 1
                break
            else:
                i = i + 1
        if leap == 0:
            print("没有此学生学号，删除失败！")
        else:
            del students[i]
            print("删除成功！")
    elif key == 3:
        print("您选择了修改学生信息功能")
        alterId = input("请输入你要修改学生的学号:")
        # 检测是否有此学号，然后进行修改信息
        i = 0
        leap = 0
        for temp in students:
            if temp['id'] == alterId:
                leap = 1
                break
            else:
                i = i + 1
        if leap == 1:
            while True:
                alterNum = int(input(" 1.修改学号\n 2.修改姓名 \n 3.修改学院 \n 4.修改地址\n 5.修改填报时间\n 6.修改健康状况\n 7.退出修改\n"))
                if alterNum == 1:
                    newId = input("输入更改后的学号:")
                    # 修改后的学号要验证是否唯一
                    i = 0
                    leap1 = 0
                    for temp1 in students:
                        if temp1['id'] == newId:
                            leap1 = 1
                            break
                        else:
                            i = i + 1
                    if leap1 == 1:
                        print("输入学号不可重复，修改失败！")
                    else:
                        temp['id'] = newId
                        print("学号修改成功")
                elif alterNum == 2:
                    newName = input("输入更改后的姓名:")
                    temp['name'] = newName
                    print("姓名修改成功")
                elif alterNum == 3:
                    newcollege = input("输入更改后的学院:")
                    temp['college'] = newcollege
                    print("学院修改成功")
                elif alterNum == 4:
                    newaddress = input("输入更改后的地址:")
                    temp['address'] = newaddress
                    print("地址修改成功")
                elif alterNum == 5:
                    newtime = input("输入更改后的填报时间:")
                    temp['time'] = newtime
                    print("填报时间修改成功")
                elif alterNum == 6:
                    newhealthy = input("输入更改后的学院:")
                    temp['healthy'] = newhealthy
                    print("健康状况修改成功")
                elif alterNum == 7:
                    break
                else:
                    print("输入错误请重新输入")
        else:
            print("没有此学号，修改失败！")
    elif key == 4:
        print("您选择了查询学生信息功能")
        searchID = input("请输入你要查询学生的学号:")
        # 验证是否有此学号
        i = 0
        leap = 0
        for temp in students:
            if temp['id'] == searchID:
                leap = 1
                break
            else:
                i = i + 1
        if leap == 0:
            print("没有此学生学号，查询失败！")
        else:
            print("找到此学生，信息如下：")
            print("学号：%s\n姓名：%s\n学院：%s\n地址：%s\n填报时间：%s\n健康状况：%s\n" % (temp['id'], temp['name'], temp['college'],temp['address'],temp['time'],temp['healthy']))
    elif key == 5:
        # 遍历并输出所有学生的信息
        print('*' * 20)
        print("接下来进行遍历所有的学生信息...")
        print("id     姓名     学院      地址      填报时间      健康状况 ")
        for temp in students:
            print("%s     %s     %s    %s    %s     %s" % (temp['id'], temp['name'], temp['college'],temp['address'],temp['time'],temp['healthy']))
        print("*" * 20)
    elif key == 6:
        # 存储学生信息
        def save_info(student_info):
            try:
                students_txt = open("D：students.txt", "w")  # 以写模式打开，并清空文件内容
            except Exception as e:
                students_txt = open("D：students.txt", "x")  # 文件不存在，创建文件并打开
            for info in student_info:
                students_txt.write(str(info) + "\n")  # 按行存储，添加换行符
            students_txt.close()
    elif key == 7:
        # 退出功能，尽量往不退出的方向引
        quitconfirm = input("真的要退出系统吗 （yes或者no）?")
        if quitconfirm == 'yes':
            print("欢迎使用本系统，谢谢")
            break;
        elif quitconfirm == "no":
            print("请选择你要执行的操作：")
        else:
            print("输入有误！")
    else:
        print("您输入有误，请重新输入")
