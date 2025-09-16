balance = 1000

def take_option():
    option = input("Enter the option: ")
    return option

def print_menu():
    menu = """
    ------------------
    SIMPLE ATM SYSTEM
    ------------------
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit
    """
    print(menu)

def option1():
    print(f"The balance is Rs. {balance}")

def option2(amount):
    global balance
    balance = balance + amount
    print(f"{amount} successfully added to balance. The new balance is {balance}")

def option3(amount):
    global balance
    if amount > balance:
        print("Cannot withdraw amount that exceeds the balance")
    else:
        balance = balance - amount
        print(f"{amount} successfully withdrawed from balance. The new balance is {balance}")


def main(option):
    if option == "1":
        option1()

    elif option == "2":
        amount = int(input("Enter amount to deposit: "))
        option2(amount=amount)

    elif option == "3":
        amount = int(input("Enter amount to withdraw: "))
        option3(amount=amount)

    elif option == "4":
        print("Thank you for using the ATM.")

    else:
        print("Invalid option. Please try again.")


option = ""

while option != "4":
    print_menu()
    option = take_option()
    main(option=option)