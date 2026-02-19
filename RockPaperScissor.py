import random
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: "))
rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\

'''
paper = '''
                             
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              

'''
scissors = '''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
                            
'''
computer_choice = ['rock', 'paper', 'scissors']
random_choice = random.choice(computer_choice)
if user_choice == 0:
    print(rock)
    print("Computer chooses:")
    if random_choice == "rock":
        print(rock)
        print("Tie!")
    elif random_choice == "paper":
        print(paper)
        print("Computer wins!")
    else:
        print(scissors)
        print("You win!")
elif user_choice == 1:
    print(paper)
    print("Computer chooses:")
    if random_choice == "rock":
        print(rock)
        print("You win!")
    elif random_choice == "paper":
        print(paper)
        print("Tie!")
    else:
        print(scissors)
        print("Computer wins!")
else:
    print(scissors)
    print("Computer chooses:")
    if random_choice == "rock":
        print(rock)
        print("Computer wins!")
    elif random_choice == "paper":
        print(paper)
        print("You win!")
    else:
        print(scissors)
        print("Tie!")

