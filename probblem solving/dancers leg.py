legs=[]
i=1
leg_change_count=0
instructions=[x for x in input("Instructions: ").split(',') if x in ["up","down","left","right"]]
print(instructions)
if len(instructions)<= 1:# for single or no instructions like {left} or {}
    print("no legs changed")
    exit(1)
instructions.append(instructions[-1])# to avoid index out of bound error during 2nd for loop 
print(instructions)
legs.append(instructions[0])
for i in range(1,len(instructions)):# this loop is to ensure no two legs present in same box like {left,left}
    if instructions[i]!=legs[0]:
        legs.append(instructions[i])
        break
print("\n\ninitial leg pairs                               = ",legs)
for i in range(2,len(instructions)-1):
    
    if instructions[i] in legs:
        print(f"incoming instruction     **{instructions[i]}**   in index {i},         updated leg pairs = {legs}")
        continue
    else:
        if instructions[i+1] in legs:
            if legs[0]==instructions[i+1]:
                legs[1]=instructions[i]
                print(f"incoming instruction     **{instructions[i]}**   in index {i},         updated leg pairs = {legs} **changed**")
                leg_change_count+=1 
            else:
                legs[0]=instructions[i]
                print(f"incoming instruction     **{instructions[i]}**  in index {i},       updated leg pairs = {legs} **changed**")
                leg_change_count+=1
        else:
            legs[0]=instructions[i]
            leg_change_count+=1
            print(f"incoming instruction     **{instructions[i]}**   in index {i},       updated leg pairs = {legs}  **changed**")
print("\nlegs changed = ",leg_change_count)
print("\nfinal leg pairs = ",legs)
print("\ntotal instructions:",instructions[:-1])