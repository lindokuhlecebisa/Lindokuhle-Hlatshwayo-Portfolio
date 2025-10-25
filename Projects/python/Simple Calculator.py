def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers, handling division by zero."""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def main():
    """
    Main function to run the simple calculator.
    It prompts the user for an operation and two numbers, then prints the result.
    """
    print("Welcome to the Simple Calculator!")
    print("Available operations: +, -, *, /")
    
    while True:
        # Prompt user for the operation
        operation = input("Enter operator (+, -, *, /) or 'q' to quit: ")
        
        # Check if the user wants to quit
        if operation.lower() == 'q':
            print("Goodbye!")
            break
        
        # Check if the operator is valid
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operator. Please try again.")
            continue
            
        try:
            # Get the numbers from the user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform the calculation based on the chosen operation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            
            # Print the result
            print(f"Result: {num1} {operation} {num2} = {result}")

        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter valid numbers.")
        
        print("-" * 20) # A separator for clarity

if __name__ == "__main__":
    main()
