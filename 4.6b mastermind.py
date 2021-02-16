#this list is only to comple the requiremnt to use a list
uselessList = []

import random #allows me to get random numbers
import sys #allows me to exit code
colors = ("blue", "white", "green", "yellow", "red", "black")
#create a dictionary with the code
code = {
    "1" : random.randrange(1, 9),
    "2" : random.randrange(1, 9),
    "3" : random.randrange(1, 9),
    "4" : random.randrange(1, 9),
    "turn" : 0
}

#testing
'''
print(code["1"])
print(code["2"])
print(code["3"])
print(code["4"])
'''

def codeCheck (num1, num2, num3, num4):
    count = 0
    if num1 == code["1"] or num1 == code["2"] or num1 == code["3"] or num1 == code["4"]:
        count += 1
    if num2 == code["1"] or num1 == code["2"] or num1 == code["3"] or num1 == code["4"]:
        count += 1
    if num3 == code["1"] or num1 == code["2"] or num1 == code["3"] or num1 == code["4"]:
        count += 1
    if num4 == code["1"] or num1 == code["2"] or num1 == code["3"] or num1 == code["4"]:
        count += 1
    if count != 4:
        code["turn"] += 1
    return count

def locationCheck (num1, num2, num3, num4):
    locationCount = 0
    if num1 == code["1"]:
        locationCount += 1
    if num2 == code["2"]:
        locationCount += 1
    if num3 == code["3"]:
        locationCount += 1
    if num4 == code["4"]:
        locationCount += 1
    return locationCount

def play():
    print(f"Turn {code['turn']}")
    num1 = (input("Whats your first number?: "))
    num2 = int(input("Whats your second number?: "))
    num3 = int(input("Whats your third number?: "))
    num4 = int(input("Whats your fourth number?: "))
    count = codeCheck(num1, num2, num3, num4)
    locationCount = locationCheck(num1, num2, num3, num4)
    print(f"You correctly guessed {count} numbers, with {locationCount} correct locations!")
    if count == 4 and locationCount == 4:
        print(f"You won in {code['turn']} turns!")
        exit(0)
    else:
        print("Try Again")

for _ in range(10):
    play()

print("You ran out of turns")
    
    
