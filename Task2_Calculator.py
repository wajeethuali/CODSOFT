# Function to display the menu options
def display_menu():
    print("\n--- Task 2: Basic Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor Division")
    print("8. All Operation")
    print("9. Exit")


# Addition
def addition():
    a = float(input("Enter 1st Number: \n"))
    b = float(input("Enter 2nd Number: \n"))
    print(f"Addition: {a} + {b} = {a + b}")


# Subtraction
def subtraction():
    a = float(input("Enter 1st Number: \n"))
    b = float(input("Enter 2nd Number: \n"))
    print(f"Subtraction: {a} - {b} = {a - b}")


# Multiplication
def multiplication():
    a = float(input("Enter 1st Number: \n"))
    b = float(input("Enter 2nd Number: \n"))
    print(f"Multiplication: {a} * {b} = {a * b}")


# Division
def division():
    a = float(input("Enter 1st Number: \n"))
    b = float(input("Enter 2nd Number: \n"))
    if b != 0:
        print(f"Division: {a} / {b} = {a / b}")
    else:
        print("Error! Division by zero is not allowed.")


# Modulus
def modulus():
    a = float(input("Enter 1st Number: \n"))
    b = float(input("Enter 2nd Number: \n"))
    if b != 0:
        print(f"Modulus: {a} % {b} = {a % b}")
    else:
        print("Error! Division by zero is not allowed.")


# Exponentiation
def exponentiation():
    a = float(input("Enter 1st Number: \n"))
    b = float(input("Enter 2nd Number: \n"))
    print(f"Exponentiation: {a} ** {b} = {a ** b}")


# Floor Division
def floor_division():
    a = float(input("Enter 1st Number: \n"))
    b = float(input("Enter 2nd Number: \n"))
    if b != 0:
        print(f"Floor Division: {a} // {b} = {a // b}")
    else:
        print("Error! Division by zero is not allowed.")


# All Operation
# Define a function to perform all operations
def all():
    a1 = float(input("Enter 1st Number: \n"))
    b1 = float(input("Enter 2nd Number:\n"))
    
    # Perform arithmetic operations
    print(f"Addition: {a1} + {b1} = {a1 + b1}")
    print(f"Subtraction: {a1} - {b1} = {a1 - b1}")
    print(f"Multiplication: {a1} * {b1} = {a1 * b1}")
    
    # Handle division and modulus carefully to avoid division by zero
    if b1 != 0:
        print(f"Division: {a1} / {b1} = {a1 / b1}")
        print(f"Modulus: {a1} % {b1} = {a1 % b1}")
        print(f"Floor Division: {a1} // {b1} = {a1 // b1}")
    else:
        print("Division, Modulus, and Floor Division: Error! Division by zero is not allowed.")
    
    # Exponentiation
    print(f"Exponentiation: {a1} ** {b1} = {a1 ** b1}")




# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-9): \n").strip()

    if choice == "1":
        addition()
    elif choice == "2":
        subtraction()
    elif choice == "3":
        multiplication()
    elif choice == "4":
        division()
    elif choice == "5":
        modulus()
    elif choice == "6":
        exponentiation()
    elif choice == "7":
        floor_division()
    elif choice == "8":
        all()

    elif choice == "9":
        print("Exiting Calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
