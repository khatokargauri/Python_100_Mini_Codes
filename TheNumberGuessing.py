import random
def compare(attempts):
    while attempts > 0:
        guess = int(input("Make a guess:"))
        if guess == random_number:
            print("You guessed right!")
            game_over = True
            return
        elif guess > random_number:
            attempts -= 1
            print(f"Too high!\nGuess again.\nYou have {attempts} attempts left!")
        else:
            attempts -= 1
            print(f"Too low!\nGuess again.\nYou have {attempts} attempts left!")
    print("You have run out of lives!")
    print("The number was " + str(random_number))
print("Welcome to the Number Guessing Game!\nI'm thinking a number between 1 and 100.")
random_number = random.randint(1, 100)
user_choice = "y"
while user_choice == "y":
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        print("You have have 10 attempts to guess!")
        compare(10)
    else:
        print("You have have 5 attempts to guess!")
        compare(5)
    user_choice = input("Do you want to play again? Type 'y' or 'n': ")



