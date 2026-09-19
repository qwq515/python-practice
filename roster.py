#困困困
lst = []

def check(value,add):
    try:
        add = value(add)
        return(add)
    except ValueError:
        return(None)

def check_age():
    while True:
        age_add = input("Please enter age:")
        age_add = check(int, age_add)
        if not age_add:
            print("Incorrect input")
            continue
        elif 0 <= age_add <= 100:
            return(age_add)
            break
        else:
            print("Incorrect number")
            continue
def check_grade():
    while True:
        grade_add = input("Please enter grade:")
        grade_add = check(float, grade_add)
        if not grade_add:
            print("Incorrect input")
            continue
        elif 0 < grade_add < 100:
            return(grade_add)
            break
        else:
            print("Incorrect number")
            continue
while True:
    order = input("请输入命令：")
    
    if order == "quit":
        for student in lst:
            print(
                student["name"],
                student["age"],"岁",
                student["grade"],"分"
            )                
        break
    elif order =="add":
        inf = {"name":"","age":0,"grade":0.0}
        
        name_add = input("请输入姓名:")
        inf["name"] = name_add
        
        '''while True:
            age_add = input("请输入年龄:")
            age_add = check(int, age_add)
            if age_add is None:
                print("年龄格式错误")
                continue       
            elif  0 < age_add < 100:   
                inf["age"] = age_add
                break
            else:
                print("无效年龄")   #一样，不知道怎么重新输入年龄
                continue
        
        while True:
            grade_add = input("请输入成绩:")
            grade_add = check(float,grade_add)
            if grade_add is None:
                print("成绩格式错误")
                continue
            elif 0 <= grade_add <= 100:     #python支持连续比较
                inf["grade"] = grade_add  
                break          
            else:
                print("无效成绩")
                continue'''
        inf["age"] = check_age()
        inf["grade"] = check_grade()   
        lst.append(inf)
        continue        
    elif order == "show":
        for student in lst:
            print(
                student["name"],
                student["age"],"岁",
                student["grade"],"分"
            )
    elif order == "find":
        f_name = input("请输入姓名:")
        found = None
        for dic in lst:
            if f_name == dic["name"]:       #检索
                found = dic
                print("姓名:", found["name"])
                print("年龄:", found["age"])
                print("成绩:", found["grade"])   
        if not found:
            print("找不到")

    elif order == "del":
        d_name = input("请输入姓名")
        found = None
        for dic in lst:
            if d_name == dic["name"]:
                found = dic
                lst.remove(dic)
                print("已删除")
                break
        if not found:
            print("找不到")

    