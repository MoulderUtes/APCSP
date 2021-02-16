program = input("What program do you want to run? (1,2,3): ")

if program == "1":
    #program 1
    print ("1")
    number = input("Choose a number between 1/100: ")
    while int(number) < 1 or int(number) > 100:
        print("Invalid Number!")
        number = input("Choose a number between 1/100: ")
    print("Thanks for your input!")
elif program == "2":
    #program 2
    print("2")
    guessCount = 1
    guess = input("Whats my favorite color?: ")
    print(guess)
    while guess != "Red" and guess != "red":
        print("Wrong Try again")
        guess = input("Whats my favorite color?: ")
        guessCount += 1
    print("Correct!, it took you, " + str(guessCount) + " attempts.")
elif program == "3":
    #program 3
    print("3")
    numSum = 0
    numCount = int(input("How many numbers do you have?: "))
    for X in range(numCount):
        X = int(input("What the first/next nubmer?: "))
        numSum += X
    print("Your sum is " + str(numSum))
else:
    print("Invalid Choice!")


