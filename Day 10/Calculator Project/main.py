from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    should_accumulate = True
    first_num = float(input("What is the first number? "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_choice = input("Pick an operation: ")
        second_num = float(input('What is the next number? '))

        answer = operations[operation_choice](first_num, second_num)
        print(f"{first_num} {operation_choice} {second_num} = {answer}")

        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if continue_calc == 'y':
            first_num = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
