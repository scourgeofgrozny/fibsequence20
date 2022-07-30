import time
from sequence import fiblist

while True:
    try:
        num=int(input("Enter a number from 1-20 digits "))
        if not (1<=num<=20):
            raise ValueError()
        break
    except ValueError:
        print("Please enter a valid number")

if num in fiblist:
    print("Your number is part of the Fibanocci sequence","\n",
    f"Your number: {num}")
    time.sleep(5)
    
elif num>10**20:
    print("Number is too large (not between 1 and 10^20)","\n",
    f"Your number: {num}")
    time.sleep(5)
    
elif num<1:
    print("Enter a positive number lol","\n",
    f"Your number: {num}")
    time.sleep(5)
    
if num not in fiblist:
    print("Your number is not part of the Fibanocci sequence","\n",
    f"Your number: {num}")
    time.sleep(5)