# Objective: The aim of this assignment is to build a basic calculator that can 
# perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

# Task 2: Use inputs to ask the user what operation they want to perform, 
# and what numbers they want to use.

# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.


# Define arithmetic functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Function to display the menu
def display_menu():
    print("\n--- Simple Calculator ---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main function to handle the calculator logic
def main():
    while True:
        # Display menu options
        display_menu()

        # Get user choice
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                # Get user input for numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            # Perform the selected operation
            if choice == '1':
                print(f"The result of addition: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of multiplication: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of division: {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")

# Call the main function to run the calculator
if __name__ == "__main__":
    main()
   
