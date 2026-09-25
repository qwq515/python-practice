#import json
import todo_utils
#utility functions

#functional functions

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

