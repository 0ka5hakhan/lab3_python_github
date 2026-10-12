def add(a, b):
    return a + b
 
 
def subtract(a, b):
    return a - b
 
 
def multiply(a, b):
    return a * b
 
 
def divide(a, b):
    if b == 0:
        return None  # signals division by zero
    return a / b
 
 
def check_even_odd(n):
    if n != int(n):
        return "not a whole number, so it is neither even nor odd"
    return "even" if int(n) % 2 == 0 else "odd"
 
 
def percentage(a, b):
    """Return what percent a is of b."""
    if b == 0:
        return None
    return (a / b) * 100
 
 
def get_number(prompt):
    """Keep asking until the user types a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a number (e.g. 5, -3, 2.5).")
 
 
def show_menu():
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")
    print("=============================")
 
 
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()
 
        if choice == "7":
            print("Thank you for using the calculator. Goodbye!")
            break
 
        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Invalid choice. Please select a number from 1 to 7.")
            continue
 
        if choice == "5":
            n = get_number("Enter a number: ")
            print(f"Result: {n:g} is {check_even_odd(n)}.")
            continue
 
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
 
        if choice == "1":
            print(f"Result: {a:g} + {b:g} = {add(a, b):g}")
        elif choice == "2":
            print(f"Result: {a:g} - {b:g} = {subtract(a, b):g}")
        elif choice == "3":
            print(f"Result: {a:g} × {b:g} = {multiply(a, b):g}")
        elif choice == "4":
            result = divide(a, b)
            if result is None:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {a:g} ÷ {b:g} = {result:g}")
        elif choice == "6":
            result = percentage(a, b)
            if result is None:
                print("Error: Cannot calculate a percentage of zero.")
            else:
                print(f"Result: {a:g} is {result:g}% of {b:g}")
 
 
if __name__ == "__main__":
    main()
