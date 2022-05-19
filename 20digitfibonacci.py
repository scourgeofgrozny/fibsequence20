import time
from sequence import fiblist
num=int(input("Enter a number from 1-20 digits "))
count=0 
while count!=0:
    break
if num in fiblist:
    print("Your number is part of the Fibanocci sequence","\n","Your number: ",num)
    time.sleep(5)
    count+1
elif num>10**20:
    print("Number is too large (not between 1 and 10^20)","\n","Your number: ",num)
    time.sleep(5)
    count+1
elif num<1:
    print("Enter a positive number lol","\n","Your number: ",num)
    time.sleep(5)
    count+1
if num not in fiblist:
    print("Your number is not part of the Fibanocci sequence","\n","Your number: ",num)
    time.sleep(5)
    count+1
