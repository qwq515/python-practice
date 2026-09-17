order = input("请输入指令：")
balance = 1000
def deposit(a,b):
    c = a+b
    return(c)
def withdraw(a,b):
    if a > b:
        print("取出的钱不能大于本金哦")
    else:
        c = b - a
        return(c)
def show_balance(a):
    reutrn(a)
while order != "q":
    if order == "d":
        dep = int(input("存入金额："))
        balance = deposit(balance,dep)
        print("存款成功")
        continue
    elif order == "w":
        wid = int(input("取款金额："))
        balance = withdraw(balance,wid)
        print("取款成功")
        continue
    elif order == "s":
        sh = show_balance(balance)
        print("当前金额：",sh)
        continue