# Guess the number game
print("Do you want to play guess the number game?")
print("If the answer is yes please enter yes otherwise enter no.")
while True:
    answer = input("Your answer:")
    if answer == "no":
        print("Ok, another time.")
        break
    elif answer == "yes":
        while True:
            number = 9631   # write the number your friend have to guess

            gouess = int(input("Type your guess:"))
            if number > gouess:
                print("Please enter higher number")
            elif number < gouess:
                print("Please enter lower number")
            elif number == gouess:
                print("Congrats! You won:)")
                break
    else:
        print("Invalid. Please try again.")
        continue
    break
