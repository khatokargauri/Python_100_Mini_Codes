import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']
word_list = ["apple", "banana", "cherry", "dragon", "elephant", "forest", "galaxy", "horizon", "island", "jungle"]
lives = 6
choosen_word = random.choice(word_list)
placeholder = ""
length = len(choosen_word)
for i in range (length):
    placeholder += "_"
print(placeholder)
# TODO - 1 - Use a while loop to let the user guess again.
correct_list = []
game_over = False
while not game_over:
    print(f"{lives} lives left")
    guess = input("Guess a letter: ").lower()
    if guess in correct_list:
        print("You have already guessed this letter!")
    display = ""
# TODO - 2 - Change the for loop so that you keep the previous
    for i in choosen_word:
        if i == guess:
            display += i
            correct_list.append(i)
        elif i in correct_list:
            display += i
        else:
            display += "_"
    print(display)
    if guess not in choosen_word:
        print(f"You guessed {guess}, that is not in the word\n You lose a life!")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")
    if "_" not in display:
        game_over = True
        print("You win")
    print(stages[lives])
print(f"The word is {choosen_word}")