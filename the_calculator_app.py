# Objective: The aim of this assignment is to build a basic calculator that can 
# perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

# Task 2: Use inputs to ask the user what operation they want to perform, 
# and what numbers they want to use.

# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

num1 = int(input("Enter first number: "))
operator = input("Enter your operator: ")
num2 = int(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print ("invalid operator")