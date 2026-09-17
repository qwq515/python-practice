lst = []

while True:

   num = input("请输入分数或输入quit退出：")
  
   if num == "quit":
       print("退出")
       break
   elif num == "del":
       if not lst:
         print("目前没有数据可以删除哦")
       else:
         del lst[-1]
         print("上一个数据已删除")
         continue
   try:
       num_cl = float(num)
       lst.append(num_cl)

   except ValueError:
       print("请输入数字")

print(lst)

def my_max(grade):
    if not grade:
        print("没有成绩哦")
    else:
        g_max = grade[0]

        for i in grade:
            if i >g_max:
           
                g_max = i
        return(g_max)

final=my_max(lst)

if final is None:
    pass

else:
    print("最高分为",final)
#Its good enough
