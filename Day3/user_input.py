dish_name = input("Enter your dish name: ")
dish_price = input("Enter your dish price: ")

dish_price = float(dish_price)

discount = input("Enter your discount in %: ")
discount = float(discount)

discount_price = (discount/100) * dish_price
final_price = dish_price - discount_price

print(f"Hello, {dish_name} initial price was {dish_price}, after a discount of {discount}%, the final price is {final_price}")