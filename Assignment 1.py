while True:

    print("\n===== SIMPLE CALCULATOR =====")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /, %, ): ")

    if operator == "+":
        print("Answer =", num1 + num2)

    elif operator == "-":
        print("Answer =", num1 - num2)

    elif operator == "*":
        print("Answer =", num1 * num2)

    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Answer =", num1 / num2)

    elif operator == "%":
        print("Answer =", num1 % num2)

    elif operator == "":
        print("Answer =", num1 ** num2)

    else:
        print("Invalid Operator")

    again = input("Do you want to continue? (yes/no): ")

    if again.lower() != "yes":
        print("Calculator Closed")
        break