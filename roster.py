#困困困
import json
with open("roster_student.json","r",encoding="utf-8")as f:
    lst = json.load(f)


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
while True:
    order = input("请输入命令：")
    
    if order == "quit":
        for student in lst:
            print(
                student["name"],
                student["age"],"岁",
                student["grade"],"分"
            )   
        with open("roster_student.json","w",encoding="utf_8")as f:
            json.dump(lst, f,ensure_ascii=False,indent=2)             
        break

    elif order =="add":
        inf = {"name":"","age":0,"grade":0.0}
        
        name_add = input("请输入姓名:")
        inf["name"] = name_add
        
        #var_age = "age"
        #var_grade = "grade"
        inf["age"] = check_age_grade("age",int,0,100,False,False)
        inf["grade"] = check_age_grade("grade",float,0,100,True,True)   
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

    