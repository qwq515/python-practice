balance = 1000
def deposit(a,b):
    c = a+b
    return(c)
def withdraw(a,b):
        c = b - a
        return(c)
def show_balance(a):
    return(a)

while True:
    order = input("请输入指令：")
    if order == "q":
        print("退出")    
        break
    elif order == "d":
        dep = int(input("存入金额："))
        balance = deposit(balance,dep)
        print("存款成功")
        continue
    elif order == "w":
        wid = int(input("取款金额："))
        if wid > balance:
            print("取款金额不能大于存款金额")
            continue
        else:
            balance = withdraw(wid,balance)
            print("取款成功")
        continue
    elif order == "s":
        sh = show_balance(balance)
        print("当前金额：",sh)
        continue