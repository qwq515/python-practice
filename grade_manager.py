lst = []

while True:

    grade = input("请输入数字或命令（命令提示输help）:")

    if grade == "help":
        print("quit停止输入\ndel删除上一个数据")
        print("show显示已有成绩")
        continue
    elif grade == "quit":
        break
    elif grade == "del":
        if not lst:
            print("还没有数值哦")
        else:
            del_item = lst.pop()
            print("已删除",del_item)
        continue
    elif grade == "show":
        print(lst)
        continue
    try :
        grade_cl = float(grade)
        lst.append(grade_cl)

    except ValueError:
        print("请输入数字哦")

def my_cal(grade):
    if not grade:
        pass
    else:
        g_max = grade[0]
        g_min = grade[0]
        g_sum = 0.00
        g_len = len(grade)
        i = 0.00
        for i in grade:
            g_sum += i
            if i > g_max:
                g_max = i
            elif i < g_min:
                g_min = i
    g_avg = g_sum/g_len
    return(g_max,g_min,g_avg)
'''final_max = my_max(lst)
final_min = my_min(lst)
fianl_avg = my_avg(lst)
if not final_avg:
    print("没有数据哦")
else:
    print("最大值",final_max)
    print("最小值",final_min)
    print("平均数",fianl_avg)


def my_min(grade):
    if not grade:
        pass
    else:
        g_min = grade[0]
            
        for i in grade:
            if i < g_min:
                g_min = i
        return(g_min)

def my_max(grade):
    if not grade:
        pass
           
    else:
        g_max = grade[0]

        for i in grade:
          
            if i > g_max:
                 g_max = i

        return(g_max)
def my_avg(grade):
    if not grade:
        pass
    else:
        for i in grade:
            g_len = len(lst)
            g_sum = 0.00
            g_abg = 0.00
            g_sum += i
        g_avg = g_sum/g_len
        return(g_avg)'''
if not lst:
    print("没有数据哦")
else:
    final_max,final_min,final_avg = my_cal(lst)
    if not final_avg:
     print("没有数据哦")
    else:
        print("最大值",final_max)
        print("最小值",final_min)
        print("平均数",final_avg)
