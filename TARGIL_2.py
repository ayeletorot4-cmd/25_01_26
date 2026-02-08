#TARGIL
#input number
#אם המספר מתחלק ב2 תדפיס זוגי
#אם המספר מתחלק ב3 תדפיס 3
#אחרת תדפיס  not divided by 2 and 3
num= int(input("Enter a number"))
if num%2==0:
    print("even")
elif num%3==0:
    print(3)
else:
    print("not divided by 2 and 3")