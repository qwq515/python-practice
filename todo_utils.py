def done(todo_lst):
    found_item = input("please enter your goal item:")
    found1 = None
    for num,things in todo_lst.items():
        if found_item == things["items"]:
            print(things["items"],"| finish time:",things["finish time"],num)   
            found1 = True
    if found1 is None:
        print("cannot find this item")
        return
    while True:
        del_num = input("please enter your goal number:")
        try:
            del_num = int(del_num)
            if del_num not in todo_lst:
                print("invalid task number")
                continue
        
            if todo_lst[del_num]["items"] == found_item:
                todo_lst[del_num]["completed"] = True
                return
            else:
                print("wrong")
                continue
        except ValueError:
            print("wrong input")
            

def show(todo_lst):
    for num,things in todo_lst.items():
        if things["completed"] == False:
            print("[ ]",things["items"],"| finish time:",things["finish time"])
        if things["completed"] == True:
            print("[✓]",things["items"],"| finish time:",things["finish time"])
