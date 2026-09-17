balance = 1000
#def valueerror(mon)

def deposit(deposit,balance):
    rest = deposit+balance
    return(rest)
def withdraw(withdraw,balance):
        rest = balance - withdraw
        return(rest)
def show_balance(mon):
    return(mon)

while True:
    order = input("请输入指令：")
    if order == "q":
        print("退出")    
        break
    elif order == "d":
        dep = input("存入金额：")
        try:
            dep = int(dep)
            if dep <= 0:
                print("无效存款")
            else:
                balance = deposit(balance,dep)
                print("存款成功")
                continue
        except ValueError:
            print("无效输入")
            continue
    elif order == "w":
        wid = input("取款金额：")
        try:
            wid = int(wid)
            if wid <= 0:
                print("无效输入")
            else:
                if wid > balance:
                    print("取款金额不能大于存款金额")
                    continue
                else:
                    balance = withdraw(wid,balance)
                    print("取款成功")
                continue
        except ValueError:
            print("无效输入")
            continue
    elif order == "s":
        sh = show_balance(balance)
        print("当前金额：",sh)
        continue