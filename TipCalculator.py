print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill(in rupees)? "))
tip = int(input("How much tip would you like to give(in %)? "))
number_of_people = int(input("How many people to split the bill? "))
overall_bill = (total_bill + (total_bill * (tip / 100))) / number_of_people
print(f"Each person should pay rupees {overall_bill:.2f}")