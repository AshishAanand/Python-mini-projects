import random

print("Word guessing game")
name = input("What's your name: ")
print(f"Best of luck, {name}!")

word_list = [
    "Ashish", "Superman", "Ironman", "Hulk", "Jarvis", "Coding", "Laptop", "Vikas", "Raj"
]

word = random.choice(word_list).lower()  # Selecting a random word and converting to lowercase
guesses = ""  # Accumulate the guessed letters here
chance = 10

while chance > 0:
    fail = 0

    # Showing the player the current word with correct guesses and underscores.
    display_word = ""
    for char in word:
        if char in guesses:
            display_word += char
        else:
            display_word += "_"
            fail += 1
    
    print(f"Word: {display_word}")  # Show current progress

    if fail == 0:  # All letters guessed correctly
        print("\nGood job, you guessed the word!")
        print(f"The word is {word}")
        break

    guess = input("Guess a character: ").lower()  # Input guess and convert to lowercase

    if guess in guesses:
        print("You've already guessed that letter!")
    elif guess in word:
        guesses += guess
        print("Good guess!")
    else:
        chance -= 1
        print("Wrong guess!")
        print(f"You have {chance} chances left.")

        if chance == 0:
            print("You lose!")
            print(f"The word was {word}.")
