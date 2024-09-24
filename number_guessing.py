import random as r

print("Guess the number")

random_num = r.randrange(1, 100)

while True:

    user_input = int(input("Guess the number between 1 to 100: "))

    if user_input  == random_num:
        print("You guessed it right!")
        break
    elif user_input > random_num:
        print("Too high, try again!")
    elif user_input < random_num:
        print("Too low, try again!")
    else:
        print("Invalid input, try again!")


