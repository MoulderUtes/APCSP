#4.6 edhesive procedural abstraction
import random


# defining the function compare
def compare(num1, num2): 
    if num1 < num2:
        return f"{num1} is smaller than {num2}"
    elif num2 < num1:
        return f"{num2} is smaller than {num1}"
    else:
        return f"{num1} is equal to {num2}"



#first function for 3
for _ in range(3):
    input1 = int(input("What's your first number: "))
    input2 = int(input("What's your second number: "))
    print(compare(input1, input2))



#create the list called names
names = []

#define funtion eliminate
def eliminate(count, list):
    random.shuffle(list)
    for _ in range(count):
        list.pop()
    return list
#second function for 6 times
for _ in range(6):
    names.append(input("What is a name: "))


#ask for the vote off count
offCount =  int(input("How many People would you like to vote off?: "))
print(eliminate(offCount, names))