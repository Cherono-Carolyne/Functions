def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price
    
try:
    original_price = float(input("100"))
    discount_percentage = float(input("25 "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if discount_percentage >= 20:
        print(f"$75{final_price:.2f}")
    else:
        print(f"$50{final_price:.2f}")

except ValueError:
    print("100, 25")
