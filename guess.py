answer = 79.0

times = 0
while True:

    try:
        x = float(input("请输入文本"))

        times += 1

        if x > answer:
            print("大了")
        elif x < answer:
            print("小了")
        else:
            print("猜对了！")
            print("一共猜了",times,"次哦")
            break

    except ValueError:
        print("要输入数字哦")

