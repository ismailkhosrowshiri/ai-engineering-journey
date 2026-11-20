def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """Return the difference between two numbers."""
    return first_number - second_number


def multiply(first_number, second_number):
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number, second_number):
    """Return the quotient of two numbers."""
    if second_number == 0:
        raise ValueError("Cannot divide by zero.")
    return first_number / second_number


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(first_number, operator, second_number):
    """Calculate a result using the selected arithmetic operator."""
    if operator not in OPERATIONS:
        raise ValueError("Unsupported operator. Choose +, -, *, or /.")

    return OPERATIONS[operator](first_number, second_number)


def get_number(prompt):
    """Read a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculator():
    """Run the interactive calculator."""
    first_number = get_number("Enter the first number: ")

    while True:
        print("Available operations: " + " ".join(OPERATIONS))
        operator = input("Choose an operation (+, -, *, /): ").strip()

        second_number = get_number("Enter the next number: ")

        try:
            result = calculate(first_number, operator, second_number)
        except ValueError as error:
            print(error)
            continue

        print(f"{first_number:g} {operator} {second_number:g} = {result:g}")

        choice = input(
            "Type 'y' to continue with the result, "
            "'n' to start a new calculation, or 'q' to quit: "
        ).strip().lower()

        if choice == "y":
            first_number = result
        elif choice == "n":
            first_number = get_number("Enter a new first number: ")
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Unrecognized choice. Starting a new calculation.")
            first_number = get_number("Enter a new first number: ")


if __name__ == "__main__":
    calculator()
