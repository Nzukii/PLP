# 1. Create a function named calculate_discount

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount
    percentage is 20% or higher.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after discount, or the original price if
               discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

 # 2. Define the discount calculation function
def calculate_discount(original_price, discount_percentage):
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    return final_price

# Prompt the user for input
try:
    original_price_input = float(input("Enter the original price of the item: "))
    discount_percentage_input = float(input("Enter the discount percentage: "))

    # Call the function and print the result
    final_price_result = calculate_discount(original_price_input, discount_percentage_input)
    print(f"The final price after applying the discount is: ${final_price_result:.2f}")

except ValueError as e:
    print(f"Invalid input: {e}")