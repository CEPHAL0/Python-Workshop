def discount_calculator(initial_price, discount_percentage):
    discount_amount = (discount_percentage / 100) * initial_price

    final_amount = initial_price - discount_amount

    # Return multiple values
    return discount_amount, final_amount


# Ask for input for the function
initial_amount = float(input("Enter the initial amount: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount_amount, final_amount = discount_calculator(initial_price=initial_amount, discount_percentage=discount_percentage)



# Print the value
print(
    f"The item price was {initial_amount}, discount amount was {discount_amount} and final price was {final_amount}"
)
