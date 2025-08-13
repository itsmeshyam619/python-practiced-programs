import csv
import json

'''headers=[x for x in input("Enter column names : ").split(',')]
print(headers)
data=[]
data.append(headers)
print(data)
no_of_columns=len(headers)
print(no_of_columns)
loop="y"
while loop.lower() == "y":
    y=[]
    for i in headers:
        x=input(f"Enter data for {i} :")
        y.append(x)
    data.append(y)
    loop =input("Enter data for another row ? (y/n)")
'''
data=[['name','age','sex'],['shyam',15,'m'],['kir',23,'m']]
print(data)

with open("try.csv",'a') as f:
    write=csv.writer(f)
    write.writerows(data)

with open("try.csv",'r') as f:
    read=csv.DictReader(f)
    for rea in read:    
        print(dict(rea))
