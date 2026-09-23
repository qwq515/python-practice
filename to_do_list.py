#import json

#utility functions

#functional functions
def done(todo_lst):
    found_item = input("please enter your goal item:")
    found1 = None
    for num,things in todo_lst.items():
        if found_item == things["items"]:
            print(things["items"],"| finish time:",things["finish time"],num)   
            found1 = 1    
    if found1 is None:
        print("cannot find this item")
    while True:
        del_num = input("please enter your goal number:")
        del_num = int(del_num)
        found2 = None
        for num,things in todo_lst.items():
            if del_num == num and found_item == things["items"]:
                todo_lst[num]["completed"] = True
                found2 = 1
        if found2 is None:
            print("wrong")
            continue
        elif found2 == 1:
            break
        

            

def show(todo_lst):
    for num,things in todo_lst.items():
        if things["completed"] == False:
            print("[ ]",things["items"],"| finish time:",things["finish time"])
        if things["completed"] == True:
            print("[✓]",things["items"],"| finish time:",things["finish time"])

#main program
lst = {}
num = 0
while True:
    order = input("please enter your order:")
    if order == "add":
        num += 1
        todo_dic = {num:{"items":"","finish time":"","completed":False}}
        todo_dic[num]["items"] = input("plsase enter your item:")
        todo_dic[num]["finish time"] = input("finish time:")
        lst.update(todo_dic)
    elif order == "show":
        show(lst)
    elif order == "done":
        done(lst)
    elif order == "quit":
        break
    else:
        print("wrong input")
        continue

