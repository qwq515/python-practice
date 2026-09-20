text = input("please enter your text:")
word_split =text.split() #word_split is a list,however, it cannot identify symnols
for word in word_split:
    count_dic = {"seen":"","times":0}
    if word not in word_split:
        count_dic["seen"] = word
        lst.append(count_dic)
    else:
        count
