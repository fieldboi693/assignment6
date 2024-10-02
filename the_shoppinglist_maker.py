# Objective: The aim of this assignment is to create a program that helps users make 
# a shopping list.

# Task 1: Write a function that lets the user add items to a list.

# Task 2: Include a function to remove items from the list.

# Task 3: Add a function that prints out the entire list in a formatted way.

shopping_list =[]
choice = input("Choose an option (1-4): ")

def show_menu():
    print("\n===== Shopping List Menu =====")
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")
    print("===============================")

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("\nShopping list:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")

def shopping_list_program():
    shopping_list = []
    while True:
       show_menu()
       choice = input("Choose an option (1-4): ")
        
if choice == '1':
            add_item(shopping_list)
elif choice == '2':
            remove_item(shopping_list)
elif choice == '3':
        view_list(shopping_list)
elif choice == '4':
            print("Exiting program. Goodbye!")
    
else:
    print("Invalid option, please choose a valid number (1-4).")


shopping_list_program()
