#困困困
lst = []

def check(value,add):
    try:
        add = value(add)
        return(add)
    except ValueError:
        return(None)
    #else :
        #print("格式错误:")
#value = inf("name")
#add = input()
while True:
    order = input("请输入命令：")
    inf = {"name":"","age":0,"grade":0.0}
    if order == "quit":
        print(lst)
        break
    elif order =="add":
        name_add = input("请输入姓名:")
        inf["name"] = name_add
        
        age_add = input("请输入年龄:")
        age_add = check(inf["age"], age_add)
        if age_add is None:
            print("姓名格式错误")
        else:
            inf["age"] = age_add
        
        grade_add = input("请输入成绩:")
        grade_add = check(inf["grade"],grade_add)
        if grade_add is None:
            print("姓名格式错误")
        else:
            inf["grade"] = grade_add 
        lst.append(inf)
        continue        
    elif order == "show":
        for dic in lst:
            for v in dic:
                print(v)   #这一个elif快给我写成shabi了，我不知道怎么实现你说的那个输出效果，可以在code_test.py里看我的心路历程
    elif order == "find":
        f_name = input("请输入姓名:")
        #while True:
        found = None
        for dic in lst:
            if f_name == dic["name"]:       #检索
                found = dic
                print(dic.values())     
                break
        if found:
            print("找不到")
        
    elif order == "del":
        d_name = input("请输入姓名")
        found = None
        for dic in lst:
            if d_name == dic["name"]:
                found = dic
                lst.pop(dic)
                print("已删除")

        if found:
            print("找不到")
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