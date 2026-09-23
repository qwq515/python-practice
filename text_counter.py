import string

text = input("please enter your text:")
#word_split =text.split() #word_split is a list,however, it cannot handle symnols

def pretreatment(sen):
    lst = []
    num = 0
    word = ""
    for char in sen:
        if char not in string.punctuation:
            if char != " ":
                num += 1
                word += char
            elif char == " ":
                lst.append(word)
                word = ""
        else:
            continue
    if word != "":
        lst.append(word)
    return(lst,num)

def times_max(lst):
    t_max = 0
    if not lst:
        return(None)
    else:
        for data in lst:
            if data["count"] > t_max:
                t_max = data["count"]
                max_data = data
        return(max_data)


lst = []
num = 0
not_num = 0
lst,t_len = text.pretreatment(text)
num = len(text)

for word in word_split:
    found = None
    for dic in lst:
        if word == dic["word"]:
            dic["count"] += 1
            found = word
            break
    if found is None:
        count_dic = {"word":word,"count":1}
        lst.append(count_dic)
        not_num += 1
max_word =times_max(lst)
if max_word is None:
    print("please enter the words")
    
else:
    print("character count:",t_len)
    print("word count",num)
    print("unique word count:",not_num)
    print("the most frequently mentioned word:",max_word)
