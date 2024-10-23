def calculate_order_total(choice, quantity):
    prices = {
        1: 200,  # Pizza
        2: 100,  # Burger
        3: 150,  # Dosa
        4: 250,  # Briyani
        5: 200   # Chicken Rice
    }
    
    total = prices.get(choice, 0) * quantity
    print(f"Total cost before discount: Rs. {total}")
    if total > 500:
        discount = total * 0.1
        total -= discount
        print(f"Discount applied: Rs. {discount}")
    return total

choice = int(input("Enter your choice (1-5): "))
quantity = int(input("Enter quantity: "))
total = calculate_order_total(choice, quantity)
print(f"Total cost after discount: Rs. {total}")
