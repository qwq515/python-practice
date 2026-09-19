'''import json #ues json toolkit

with open("roster_student.json","r",encoding="utf-8")as f: #r=read,"with" can close the json auto,as f named json f
    data = json.load(f) #convert Json test into python lists/dictionaries
    new_item = {"name":"victor","age":18,"grade":99.0}
    data.append(new_item)
with open("roster_student.json","w",encoding="utf-8")as f:  #w = write
    json.dump(data,f,ensure_ascii=False,indent=2)
'''
import json
with open("roster_student.json","r",encoding="utf-8")as f:
    data = json.load(f)
    for student in data:
        print(student["name"])
