import math
import random
from termcolor import colored

def display_banner():
    banner = """
    ================================
        Welcome to PyCalc 3000!    
        The Smart Calculator       
    ================================
    """
    print(colored(banner, 'cyan', attrs=['bold']))

def display_menu():
    menu = """
    Select an operation:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Modulus (%)
    6. Exponentiation (^)
    7. Square Root (√)
    8. Factorial (!)
    9. Logarithm (log)
    10. Random Number Mode 🎲
    11. View History
    12. Exit
    """
    print(colored(menu, 'yellow'))

def perform_operation(choice, history):
    if choice in range(1, 7):  # Basic arithmetic operations
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == 1:
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"
        elif choice == 2:
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"
        elif choice == 3:
            result = num1 * num2
            operation = f"{num1} * {num2} = {result}"
        elif choice == 4:
            if num2 == 0:
                return "Error: Division by zero is undefined."
            result = num1 / num2
            operation = f"{num1} / {num2} = {result}"
        elif choice == 5:
            result = num1 % num2
            operation = f"{num1} % {num2} = {result}"
        elif choice == 6:
            result = num1 ** num2
            operation = f"{num1} ^ {num2} = {result}"
        history.append(operation)
        return operation

    elif choice == 7:  # Square Root
        num = float(input("Enter a number: "))
        if num < 0:
            return "Error: Square root of a negative number is undefined."
        result = math.sqrt(num)
        operation = f"√{num} = {result}"
        history.append(operation)
        return operation

    elif choice == 8:  # Factorial
        num = int(input("Enter a number: "))
        if num < 0:
            return "Error: Factorial of a negative number is undefined."
        result = math.factorial(num)
        operation = f"{num}! = {result}"
        history.append(operation)
        return operation

    elif choice == 9:  # Logarithm
        num = float(input("Enter the number: "))
        base = float(input("Enter the base (e.g., 10 for log10): "))
        if num <= 0 or base <= 0:
            return "Error: Logarithm requires positive numbers."
        result = math.log(num, base)
        operation = f"log_{base}({num}) = {result}"
        history.append(operation)
        return operation

    elif choice == 10:  # Random Number Mode
        print("Random Number Mode:")
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Random numbers: {num1}, {num2}")
        return perform_operation(int(input("Choose an operation (1-6): ")), history)

    elif choice == 11:  # View History
        if not history:
            return "History is empty."
        print("\nCalculation History:")
        for index, item in enumerate(history, 1):
            print(f"{index}. {item}")
        return "End of history."

    elif choice == 12:  # Exit
        print(colored("Thank you for using PyCalc 3000!", 'green', attrs=['bold']))
        exit()

    else:
        return "Invalid choice. Please try again."

def main():
    display_banner()
    history = []

    while True:
        display_menu()
        try:
            choice = int(input(colored("Enter your choice (1-12): ", 'blue')))
            result = perform_operation(choice, history)
            if result:
                print(colored(f"Result: {result}", 'green'))
        except ValueError:
            print(colored("Invalid input! Please enter a number between 1 and 12.", 'red'))

if __name__ == "__main__":
    main()
