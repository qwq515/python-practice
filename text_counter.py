text = input("please enter your text:")
word_split =text.split() #word_split is a list,however, it cannot identify symnols

def times_max(lst):
    t_max = 0
    for data in lst:
        if data["times"] > t_max:
            t_max = data["times"]
            max_data = data
            return(max_data)
    return(None)

lst = [{"seen":"","times":0}]
num = 0
not_num = 0
text = text.replace(" ", "")
t_len = len(text)
for word in word_split:
    num += 1
    found = None
    for dic in lst:
        if word == dic["seen"]:
            dic["times"] += 1
            found = word
            break
    if found is None:
        count_dic = {"seen":word,"times":1}
        lst.append(count_dic)
        not_num += 1
max_word =times_max(lst)
if max_word is None:
    print("please enter the words")
    
else:
    print("character count:",t_len)
    print("word count",num)
    print("not repeated character count:",not_num)
    print("the most frequently mentioned word:",max_word)