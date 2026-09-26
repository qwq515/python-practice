import string

def clean(sen):
    result = []
    word = ""
    for char in sen:
        if char not in string.punctuation:
            if char != " ":
                word += char
            elif char == " ":
                result.append(word)
                word = ""
        else:
            continue
    if word != "":
        result.append(word)
    return result
sentence = input("please enter your characters")
result = clean(sentence)
#breakpoint()
result_cl = set(result)
#breakpoint()
print(result_cl)
