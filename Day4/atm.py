pin = "12345"

balance = 1000.00

print("Welcome to ATM")

unsuccessful_attempts = 0

while unsuccessful_attempts < 3:
    if unsuccessful_attempts == 0:
        input_pin = input("Enter the PIN: ")
    else:
        input_pin = input("Wrong PIN entered, Enter the PIN again: ")

    if input_pin != pin:
        unsuccessful_attempts = unsuccessful_attempts + 1
    else:
        break

if unsuccessful_attempts >= 3:
    print("You entered the wrong PIN 3 times, exiting")
else:
    print("Logged in successfully")
    print(
        """
        Menu:
            1. Withdraw Money
            2. Deposit Money
            3. Check Balance
            4. Exit
        """
    )
    option = ""

    while option != "4":
        option = input("Enter the option: ")
        if option == "1":
            withdraw_amount = float(input("Enter the amount you want to withdraw: "))

            if withdraw_amount > balance:
                print("Cannot withdraw money more than the balance")
            else:
                balance = balance - withdraw_amount
                print(f"Withdrawed {withdraw_amount} from account successfully")

        elif option == "2":
            deposit_amount = float(input("Enter the amount you want to deposit: "))
            balance = balance + deposit_amount
            print(f"Deposited {deposit_amount} successfully to the balance")
            
        elif option == "3":
            print(f"Your current balance is {balance}")
