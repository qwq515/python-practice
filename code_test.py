lst = [{"name":"zhang","age":18},{"name":"wang","age":93}]
for i in lst:
    print("\n")
    for v in i.values():
        print(v,end="")
    #print(i.values())
    #for v in i.values():
     #   print(v)
#dic = lst[0]
#print(dic.values())
#打印出来的太脏了，我们只需要值
#还是脏，那个dict为什么会出现
#为什么打印出来是竖着的
#依旧丑，甚至更丑