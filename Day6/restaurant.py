message = """
    ------------------
    WELCOME TO FOODIE HUB
    ------------------
    MENU:
    1. Burger - $35
    2. Pizza - $40
    3. Pasta - $25
    4. Soda - $10
    5. Exit
"""

number_of_orders = input("Enter the number of orders you want to take: ")
number_of_orders = int(number_of_orders)

total_bill_amount = 0
orders = []

for number in range(number_of_orders):
    print(message)
    order = int(input("Enter the item you want to order: "))

    if order == 1:
        total_bill_amount += 35
        orders.append("Burger")
    elif order == 2:
        orders.append("Pizza")
        total_bill_amount += 40
    elif order == 3:
        orders.append("Pasta")
        total_bill_amount +=25
    elif order == 4:
        orders.append("Soda")
        total_bill_amount += 10

discount = 0
discount_percentage = 0
if total_bill_amount >= 100:
    discount = total_bill_amount * 0.2
    discount_percentage = 20
elif total_bill_amount >= 50:
    discount = total_bill_amount * 0.1
    discount_percentage = 10

final_price = total_bill_amount - discount

print(f"Your orders were {orders}")
print(f"The total price was ${total_bill_amount}, discount percentage was {discount_percentage}% ,discount price was ${discount}, final price is ${final_price}")
