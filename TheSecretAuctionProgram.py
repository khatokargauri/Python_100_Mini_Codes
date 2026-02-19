bid_dictionary = {}
choice = "y"
while choice == "y":
    name = input("Type your name:\n")
    bid = int(input("Type your bid: rupees\n"))
    bid_dictionary[name] = bid
    choice = input("Are there any other bidders? (y/n)\n")
    print("\n" * 100)
max = 0
for key in bid_dictionary:
    if bid_dictionary[key] > max:
        max = bid_dictionary[key]
        winner = key
print(f"The maximum bid is rupees {max} by {winner}")
