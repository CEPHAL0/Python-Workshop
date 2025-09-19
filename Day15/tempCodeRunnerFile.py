
class Bank:
    name = ""
    currency_reserve = 0

    def set_currency_reserve(self, c):
        self.currency_reserve = c * 132




bank1 = Bank()

bank1.name = input("Enter the name of bank: ")
input_value = int(input("Enter the currency reserve: "))
bank1.set_currency_reserve(c=input_value)

print(bank1.name)
print(bank1.currency_reserve)