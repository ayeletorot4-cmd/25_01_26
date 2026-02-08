
num = int(input("Enter a number"))
i=2
if num<=1:
    print("not prime")
else:
     while num!=i:
          if num%i == 0:
             print("not prime")
             break
          #else:
             print(" prime")
             break
          i=i+1
     else:
          print(" prime")