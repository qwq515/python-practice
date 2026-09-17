balance = 1000
def check_money(mon):
    try:
        mon = int(mon)
        if mon > 0:
            return mon
        #return None
    except ValueError:
        return None
        

def deposit(balance,deposit):
    rest = balance + deposit
    return(rest)
def withdraw(balance,withdraw):
        rest = balance - withdraw
        return(rest)
#def show_balance(mon):
    #return(mon)

while True:
    order = input("请输入指令：")
    if order == "q":
        print("退出")    
        break
    elif order == "d":
        dep = input("存入金额：")
        dep = check_money(dep)
        if dep is None:
            print("无效存款")
        else:
            balance = deposit(balance,dep)
            print("存款成功")
            continue
    elif order == "w":
        wid = input("取款金额：")
        wid = check_money(wid)
        if wid is None:
            print("无效输入")
        else:
            if wid > balance:
                print("取款金额不能大于存款金额")
                continue
            else:
                balance = withdraw(balance,wid)
                print("取款成功")
                continue
    elif order == "s":
        print("当前金额：",balance)
        continue