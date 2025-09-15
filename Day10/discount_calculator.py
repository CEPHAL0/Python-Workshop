def discount_calculator():
    # Ask for the input price from user
    item_price = float(input("Enter the price of item: "))

    # Ask for the discount percentage from user
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the discount
    discount_amount = (discount_percentage/100) * item_price
    final_amount = item_price - discount_amount

    # Return multiple values
    return item_price, discount_amount, final_amount

# Call the function and retrieve the value
item_price, discount_amount, final_amount = discount_calculator()

# Print the value
print(f"The item price was {item_price}, discount amount was {discount_amount} and final price was {final_amount}")