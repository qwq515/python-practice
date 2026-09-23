#functional functions
def done(todo_lst):
    found_item = input("please enter your goal item:")
    found = None
    for things in todo_lst:
        if found_item == things["items"]:
            while True:  
                print("you want to change:",things)
                judgment =input("y/n")
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
    return(todo_lst)

#main program
lst = []
while True:
    order = input("please enter your order:")
    todo_dic = {"items":"","finish time":"","completed":False}
    if order == "add":
        todo_dic["items"] = input("plsase enter your item:")
        todo_dic["finish time"] = input("finish time:")
        lst.append(todo_dic)
        continue
    if order == "show":
        print(lst)
    if order == "done":
        lst = done(lst)
    if order == "quit":
        break
