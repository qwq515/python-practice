#困困困
lst = []
inf = {"name":"","age":0.0,"grade":0.0}

def check(value,add):
    try:
        add = value(add)
        return(add)
    except ValueError:
        
    #else :
        #print("格式错误:")
#value = inf("name")
#add = input()
while True:
    order = input("请输入命令：")
    if order == "quit":
        print(lst)
        break
    elif order =="add":
        name_add = input("请输入姓名")
        inf["name"] = check(inf["name"],name_add)
        if inf["name"] is None:
            print("姓名格式错误")
            continue
        

    '''elif order == "add":
        name_add = input("请输入姓名:")
        try:
            name_add = str(name_add)
            inf["name"] = name_add
        except ValueError:
            print("格式错误：")
        age_add = input("年龄:")
        try:
            age_add = float(age_add)
            inf["age"] = age_add
        except ValueError:
            print("格式错误：")       
        grade_add = input("成绩:")
        try:
            grade_add = float(grade_add)
            inf["grade"] = grade_add
        except ValueError:
            print("格式错误：")
        lst.append(inf)
        print(type(inf["age"]))
        print(lst)'''