import csv

headers=[x for x in input("Enter column names : ").split(',')]
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
print(dict(data))


