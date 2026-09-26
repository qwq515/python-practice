sentence = input("please enter your characters:")

result =sentence.split()    #lst
'''#breakpoint()
#result_cl = set(result)     dic

result_non = []
result_dup = []
for word in result:
    if word not in result_non:
        result_non.append(word)
    else:
        result_dup.append(word)

print("origin quantity:",len(result))
print("non-duplicate quantity:",len(set(result)))
print("duplicate words:",set(result_dup))'''

result_try = {}
for word in result:
    if word not in result_try:
        result_try[word] = 1
    else:
        result_try[word] += 1

dup_word = []
for word in result_try:
    if result_try[word] != 1:
        dup_word.append(word)



print("origin quantity:",sum(result_try.values()))
print("unique quantity:",len(result_try))
print("duplicate words:",*dup_word)
