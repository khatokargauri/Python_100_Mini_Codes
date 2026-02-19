def add(n1, n2):
    return n1 + n2
# TODO : Write out the other three functions - subtract, multiply, and divide.
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
# Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
overlap = "y"
number1 = int(input("Enter the first number: "))
while overlap == "y":
    user_choice = input("Operations: +, -, *, /\nWhichone would you like to do? ")
    number2 = int(input("Enter the second number: "))
    if user_choice in operations:
        operation = operations[user_choice]
        result = operation(number1, number2)
        print(f"{number1} {user_choice} {number2} = {result}")
        number1 = result
        overlap = input(f"Do you want to continue operations with {result}?(y/n):")
        if overlap == "n":
            print("Calculation completed!")