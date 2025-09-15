def calculator():
    number1 = int(input("Enter the number 1: "))
    operator = input("Enter the operator (+,-,*,/): ")
    number2 = int(input("Enter the number 2: "))

    if operator == "+":
        final_value = number1 + number2
    elif operator == "-":
        final_value = number1 - number2
    elif operator == "*":
        final_value = number1 * number2
    elif operator == "/":
        final_value = number1 / number2
    else:
        print("The option is wrong")

    return final_value

final_value = calculator()
print(f"The final value is {final_value}")
