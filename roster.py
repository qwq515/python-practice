import json

def save_data(lst):
    with open("roster_student.json","w",encoding="utf-8")as f:
        json.dump(lst, f,ensure_ascii=False,indent=2)

def load_data():
    try:
        with open("roster_student.json","r",encoding="utf-8")as f:
            lst = json.load(f)
            return(lst)
    except FileNotFoundError:
        lst = []
        save_data(lst)
        return(lst)
    except json.JSONDecodeError:
        print("The JSON file is corrupted;please check the file")
        exit()

def check(value,add):
    try:
        add = value(add)
        return(add)
    except ValueError:
        return(None)

def check_age_grade(var,data_type,num_min,num_max,left_equal,right_equal):
    while True:
        add = input("Please enter "+var+":")       #input can only except 1 argument,use + to splice
        add = check(data_type, add)
        if add is None:
            print("Incorrect input")
            continue
        elif (num_min <= add if left_equal else num_min < add)and(add <= num_max if right_equal else add < num_max):
            return(add)
        else:
            print("Incorrect number")
            continue

def add_student(lst):
    inf = {"name":"","age":0,"grade":0.0}
        
    name_add = input("请输入姓名:")
    inf["name"] = name_add
    inf["age"] = check_age_grade("age",int,0,100,False,False)
    inf["grade"] = check_age_grade("grade",float,0,100,True,True)   
    lst.append(inf)
    save_data(lst)        
    return(lst)

lst = load_data()

while True:
    order = input("请输入命令：")
    
    if order == "quit":
        for student in lst:
            print(
                student["name"],
                student["age"],"岁",
                student["grade"],"分"
            )   
        save_data(lst)          
        break

    elif order =="add":
        lst = add_student(lst)
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
                save_data(lst)
                break
        if not found:
            print("找不到")
    elif order == "update":
        re_name = input("enter name")
        for stu in lst:
            found = None
            if re_name == stu["name"]:
                found = stu
                stu["name"] = input("new name:")
                stu["age"] = input("new age")
                stu["grade"] = input("new grade")
                save_data(lst)
        if found is None:
                print("404 not find")

    