import random

Choices = ["s" ,"p" , "x"]
userWins = 0
computerWins = 0

while True:
    print("This is the Stone/Paper/Scissors game !\n")
    print("Type [S/s] for Stone.")
    print("Type [P/p] for Paper.")
    print("Type [X/x] for Scissors.")
    print("Type 'q/Q' to end the game. \n")
    userInput = input("Enter your Choice.... : ").lower()

    if userInput == "q":
        break

    if userInput not in Choices:
        continue

    number = random.randint(0,2)
    computerChoice = Choices[number]
    print("The Computer picked ",computerChoice+".")
    if userInput == computerChoice:
        print("No points as its a Draw !")

    elif userInput == "s" and computerChoice == "x":
        print("You Chose : Stone ")
        print("Compuer Chose : Scissors ")
        print("You Won !!!")
        userWins +=1
    elif userInput == "p" and computerChoice == "s":
        print("You Chose : Paper ")
        print("Compuer Chose : Stone ")
        print("You Won !!!")
        userWins +=1
    elif userInput == "x" and computerChoice == "p":
        print("You Chose : Scissors ")
        print("Compuer Chose : Paper ")
        print("You Won !!!")
        userWins +=1

    else:
        print("You Lost !!!")
        computerWins +=1

print("SCORE BOARD. ")
print("USER :")
print("        |-----------------|")
print("        |      PLAYER     |")
print("        |    ",userWins,  "times...  |")
print("        |-----------------|")

print("COMPUTER :")
print("        |-----------------|")
print("        |     COMPUTER    |")
print("        |    ",computerWins,  "times...  |")
print("        |-----------------|")

print("GoodBye!")
