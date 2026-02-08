#START
i=0
sum=0

while i<10:
    height= int(input("enter your height: "))
    if height>= 140 and height<=190:
        i+=1
        sum+=height
    else: print("illegal height")

print(sum/10)
#STOP