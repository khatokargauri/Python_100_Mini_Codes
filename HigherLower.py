import random
data = [
    {
        "name": "Virat Kohli",
        "follower_count": 265_000_000,
        "description": "Indian cricketer and former captain",
        "country": "India"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 285_000_000,
        "description": "Singer-songwriter and global pop icon",
        "country": "USA"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 620_000_000,
        "description": "Professional footballer",
        "country": "Portugal"
    },
    {
        "name": "Emma Watson",
        "follower_count": 75_000_000,
        "description": "Actress and activist",
        "country": "UK"
    },
    {
        "name": "Elon Musk",
        "follower_count": 180_000_000,
        "description": "Entrepreneur and business leader",
        "country": "USA"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 430_000_000,
        "description": "Singer and actress",
        "country": "USA"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 500_000_000,
        "description": "Football player and world champion",
        "country": "Argentina"
    },
    {
        "name": "Priyanka Chopra",
        "follower_count": 90_000_000,
        "description": "Actress and producer",
        "country": "India"
    },
    {
        "name": "Bill Gates",
        "follower_count": 70_000_000,
        "description": "Co-founder of Microsoft",
        "country": "USA"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 390_000_000,
        "description": "Actor and former wrestler",
        "country": "USA"
    }
]
def account_info(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr}, from {account_country}"
def is_correct_choice(choice,account1,account2):
    if choice == "A":
        if account_a["follower_count"] > account_b["follower_count"]:
            print("You are correct!")
            return True
        else:
            print("Sorry, that's wrong")
            return False
    else:
        if account_b["follower_count"] > account_a["follower_count"]:
            print("You are correct!")
            return True
        else:
            print("Sorry, that's wrong")
            return False
game_over = False
count = 0
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)
while not game_over:
    user_choice = input(f"Compare A:{account_info(account_a)}\nAgainst B:{account_info(account_b)}\nWho has more followers? Type 'A' or 'B':")
    is_user_correct = is_correct_choice(user_choice,account_a,account_b)
    if is_user_correct:
        count += 1
        print(f"Score:{count}")
        account_a = account_b
        account_b = random.choice(data)
    else:
        print(f"Score:{count}")
        game_over = True


