#import json

#utility functions

#functional functions
def done(todo_lst):
    found_item = input("please enter your goal item:")
    found = None
    for things in todo_lst:
        if found_item == things["items"]:
            while True:  
                print("you want to change:",things)
                judgment =input("y/n:")
                if judgment == "y":
                    things["completed"] = True
                    found = 1
                    break
                elif judgment == "n":
                    break
                else:
                    print("invalid input")
                    continue
    if found == None:
        print("cannot find this item")

def show(todo_lst):
    for things in todo_lst:
        if things["completed"] == False:
            print("[ ]",things["items"],"| finish time:",things["finish time"])
        if things["completed"] == True:
            print("[✓]",things["items"],"| finish time:",things["finish time"])

#main program
lst = []
while True:
    order = input("please enter your order:")
    if order == "add":
        todo_dic = {"items":"","finish time":"","completed":False}
        todo_dic["items"] = input("plsase enter your item:")
        todo_dic["finish time"] = input("finish time:")
        lst.append(todo_dic)
    elif order == "show":
        show(lst)
    elif order == "done":
        done(lst)
    elif order == "quit":
        break
    else:
        print("wrong input")
        continue

