
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

# Function to perform exponentiation
def exponentiate(x, y):
    return x ** y

# Function to perform modulus operation
def modulus(x, y):
    return x % y

# Function to display the menu and get user's choice
def display_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")
    print("0. Exit")

    choice = input("Enter choice (0-6): ")
    return choice

# Calculator main function
def calculator():
    while True:
        choice = display_menu()

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice not in ('1', '2', '3', '4', '5', '6'):
            print("Invalid choice. Please enter a valid option.")
            continue
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")

        elif choice == '5':
            print(f"{num1} ** {num2} = {exponentiate(num1, num2)}")

        elif choice == '6':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")

        print()  # Blank line for better readability

# Run the calculator
calculator()