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
        todo_utils.show(lst)
    elif order == "done":
        todo_utils.done(lst)
    elif order == "quit":
        break
    else:
        print("wrong input")
        continue

#finish