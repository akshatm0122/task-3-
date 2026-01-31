import time
import sys

# Function to simulate a "typing" effect for output
def type_effect(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Function to animate the loading effect
def loading_effect():
    print("Loading", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

# Function to perform the calculation with added effects
def calculator():
    # Intro animation
    type_effect("\nWelcome to the Animated Simple Calculator!", 0.1)
    time.sleep(1)
    loading_effect()

    # Operation menu with a cool "typing" effect
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    # Get user's choice of operation
    choice = input("\nEnter choice (1/2/3/4): ")

    # User input for numbers with effects
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("\nEnter the second number: "))
    
    # Perform operation with a cool "loading" effect before showing the result
    print("\nProcessing...", end="")
    loading_effect()

    # Perform the operation based on user's choice with dynamic effects
    if choice == '1':
        result = num1 + num2
        type_effect(f"\n{num1} + {num2} = {result}", 0.1)
    elif choice == '2':
        result = num1 - num2
        type_effect(f"\n{num1} - {num2} = {result}", 0.1)
    elif choice == '3':
        result = num1 * num2
        type_effect(f"\n{num1} * {num2} = {result}", 0.1)
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            type_effect(f"\n{num1} / {num2} = {result}", 0.1)
        else:
            type_effect("\nError: Division by zero is not allowed!", 0.1)
    else:
        type_effect("\nInvalid input! Please choose a valid option.", 0.1)

    # Option to restart
    restart = input("\nWould you like to perform another calculation? (y/n): ").lower()
    if restart == 'y':
        calculator()
    else:
        type_effect("\nThank you for using the Animated Calculator! Goodbye!", 0.1)
        time.sleep(1)

# Run the calculator function
calculator()
