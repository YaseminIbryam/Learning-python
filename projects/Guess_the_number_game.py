import random

number = random.randint(1, 100)
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
