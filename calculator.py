import math
def calculator():
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")

    choice = input("\nSelect an operation (1-6): ")

    try:
        if choice == "6":   # Square Root Operation
            num = float(input("Enter a number: "))
            if num < 0:
                print("Cannot calculate square root of a negative number.")
            else:
                print("Result:", math.sqrt(num))

        elif choice in ["1", "2", "3", "4", "5"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", num1 + num2)

            elif choice == "2":
                print("Result:", num1 - num2)

            elif choice == "3":
                print("Result:", num1 * num2)

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print("Result:", num1 / num2)

            elif choice == "5":
                print("Result:", num1 ** num2)

        else:   # Handle invalid choices
            print("Invalid choice. Please select from 1 to 6.")

    except ValueError:  # Handle non-numeric input
        print("Error: Please enter valid numeric values.")

while True:
    calculator()
    again = input("\nDo you want another calculation? (y/n): ")
    if again.lower() != "y":
        print("\nThank you for using the calculator!")
        break
