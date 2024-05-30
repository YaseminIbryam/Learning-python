from random import randint


def guessing(selector, guesser):
    won = False
    number = int(input(f"{selector}, please enter a number: "))
    for number_guess in range(1, number_of_guesses + 1):
        guess = int(input(f"{guesser}, please type your guess: "))
        if number > guess:
            print("Please enter higher number")
        elif number < guess:
            print("Please enter lower number")
        elif number == guess:
            won = True
            break
    if won:
        print(f"Congrats {guesser}! You guessed the number {number} with {number_guess} guesses!")
        score[guesser] += 1
    else:
        print(f"Sorry {guesser}! Next time.")


way_of_game = int(input("1.human vs human or 2.human vs computer: "))
if way_of_game == 1:
    first_player = input("First player, please enter your name: ")
    second_player = input("Second player, please enter your name: ")
    number_of_guesses = int(input("How many guesses you want guesser to have? Please enter a number: "))
    score = {first_player: 0, second_player: 0}
    number_plays = 1
    while True:
        command = input("Type play, view the score or quit: ")
        command = command.lower()
        if command == "play":
            if number_plays % 2 != 0:
                guessing(first_player, second_player)
            else:
                guessing(second_player, first_player)
            number_plays += 1
        elif command == "view the score":
            for player, score in score.items():
                print(f"{player}: {score}")
        elif command == "quit":
            break


elif way_of_game == 2:
    number = randint(1, 100)
    while True:
        guess = int(input("Enter your guess:"))
        if guess == number:
            print('Congratulations! You guessed!')
            break
        elif guess < number:
            print("Enter a bigger number")
        elif guess > number:
            print("Enter a lower number")
        else:
            print("Try again")




