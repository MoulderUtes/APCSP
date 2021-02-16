numbers = [100,50,10,1,2,7,11,17,53,-8,-4,-9,-72,-64,-80]
names = ["Peter","Bruce","Steve","Tony","Natasha","Clint","Wanda","Hope","Danny","Carol"]
sortedNumbers = sorted(numbers)
sortedNames = sorted(names)
posNumbers = []
oddNumbers = []


def pos(list):
    for x in list:
        if x > 0:
            posNumbers.append(x)

def odd(list):
    for x in list:
        if x % 2 == 1:
            oddNumbers.append(x)
            

def sum(list):
    sum = 0
    for x in list:
        sum += x
    return sum
            
pos(numbers)
odd(numbers)

print(names[0::2])
print(posNumbers)
print(sum(numbers))
print(oddNumbers)
print(sortedNames[0:9:])
print(sortedNumbers[::10])