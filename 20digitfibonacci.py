from sequence import fiblist
num=int(input("Enter a number from 1-20 digits "))
if num in fiblist:
    print("Your number is part of the Fibanocci sequence","\n","Your number: ",num)
elif num>10**20:
    print("Number is too large (not between 1 and 10^20)","\n","Your number: ",num)
elif num<1:
    print("Enter a positive number lol","\n","Your number: ",num)
if num not in fiblist:
    print("Your number is not part of the Fibanocci sequence","\n","Your number: ",num)

