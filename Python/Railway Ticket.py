def calculate_total_cost(age, tickets):
    if age >= 60:
        price = 30
    elif age <= 12:
        price = 20
    else:
        price = 50
    return price * tickets

age = int(input("Enter your age: "))
tickets = int(input("Enter number of tickets: "))
total_cost = calculate_total_cost(age, tickets)
print(f"Total cost for {tickets} tickets: {total_cost}")
