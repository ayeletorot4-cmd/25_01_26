#TARGIL
#input number until get 0 or negative
#for each number print 1....number
num= int(input("Enter a number"))

while num>0:
    i = 1
    while i<=num:
         print(i)
         i=i+1
    num = int(input("Enter a number"))
print("finished")