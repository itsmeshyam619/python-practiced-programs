num=int(input("Enter how many words you want to store:"))
name=[]
for i in range(num):
    name1=str(input(f"enter {i} name :"))
    name.append(name1)
print(name)
print("since it is not stored in file ,so it is erased after execution")

exit=input("press any key")