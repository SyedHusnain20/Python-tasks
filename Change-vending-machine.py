# proj03_lastname.py
# Student: "your name"
# Date: November 15, 2025
# Project: Change Machine for Vending Machine Simulation

print("Welcome to the vending machine change maker program")
print("Change maker initialized.")

stock = {
    'nickels': 25,
    'dimes': 25,
    'quarters': 25,
    'ones': 0,
    'fives': 0
}

print("Stock contains:")
print(f"  {stock['nickels']} nickels")
print(f"  {stock['dimes']} dimes")
print(f"  {stock['quarters']} quarters")
print(f"  {stock['ones']} ones")
print(f"  {stock['fives']} fives")

while True:
    price_input = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
    
    if price_input.lower() == 'q':
        break  

    try:
        price_float = float(price_input)
        if price_float < 0:
            print("Error: price must be non-negative.")
            continue
    except ValueError:
        print("Error: Please enter a valid number or 'q'.")
        continue

    if (round(price_float * 100) % 5) != 0:
        print("Illegal price: Must be a non-negative multiple of 5 cents.")
        continue

    price_in_cents = round(price_float * 100)
    original_price_in_cents = price_in_cents
    
    payment_in_cents = 0
    print("\nMenu for deposits:")
    print("'n' - deposit a nickel")
    print("'d' - deposit a dime")
    print("'q' - deposit a quarter")
    print("'o' - deposit a one dollar bill")
    print("'f' - deposit a five dollar bill")
    print("'c' - cancel the purchase")

    while payment_in_cents < original_price_in_cents:
        remaining_due = original_price_in_cents - payment_in_cents
        dollars = remaining_due // 100
        cents = remaining_due % 100
        
        print(f"\nPayment due: {dollars} dollars and {cents} cents")
        
        deposit = input("Indicate your deposit: ").lower()

        if deposit == 'c':
            break

        if deposit == 'n':
            payment_in_cents += 5
            stock['nickels'] += 1
        elif deposit == 'd':
            payment_in_cents += 10
            stock['dimes'] += 1
        elif deposit == 'q':
            payment_in_cents += 25
            stock['quarters'] += 1
        elif deposit == 'o':
            payment_in_cents += 100
            stock['ones'] += 1
        elif deposit == 'f':
            payment_in_cents += 500
            stock['fives'] += 1
        else:
            print("Illegal selection:", deposit)
            continue 

    if deposit == 'c': 
        change_to_return = payment_in_cents
        print("\nPlease take the change below.")
    else: 
        change_to_return = payment_in_cents - original_price_in_cents
        if change_to_return == 0:
            print("\nNo change due.")
            print("Stock contains:")
            print(f"  {stock['nickels']} nickels")
            print(f"  {stock['dimes']} dimes")
            print(f"  {stock['quarters']} quarters")
            print(f"  {stock['ones']} ones")
            print(f"  {stock['fives']} fives")
            continue

    print("\nPlease take the change below.")
    
    total_change_value = (stock['quarters'] * 25) + (stock['dimes'] * 10) + (stock['nickels'] * 5)
    if change_to_return > 0 and total_change_value < change_to_return:
        print("Machine is out of change.")
        print("See store manager for remaining refund.")
        amount_due_dollars = change_to_return // 100
        amount_due_cents = change_to_return % 100
        print(f"Amount due is: {amount_due_dollars} dollars and {amount_due_cents} cents")
        change_to_return = total_change_value 


    quarters_dispensed = min(stock['quarters'], change_to_return // 25)
    change_to_return -= quarters_dispensed * 25
    stock['quarters'] -= quarters_dispensed
    
    if quarters_dispensed > 0:
        print(f"{quarters_dispensed} quarters")

    dimes_dispensed = min(stock['dimes'], change_to_return // 10)
    change_to_return -= dimes_dispensed * 10
    stock['dimes'] -= dimes_dispensed
    
    if dimes_dispensed > 0:
        print(f"{dimes_dispensed} dimes")

    nickels_dispensed = min(stock['nickels'], change_to_return // 5)
    change_to_return -= nickels_dispensed * 5
    stock['nickels'] -= nickels_dispensed
    
    if nickels_dispensed > 0:
        print(f"{nickels_dispensed} nickels")


    if change_to_return > 0:
        print("Machine is out of change.")
        print("See store manager for remaining refund.")
        amount_due_dollars = change_to_return // 100
        amount_due_cents = change_to_return % 100
        print(f"Amount due is: {amount_due_dollars} dollars and {amount_due_cents} cents")


    print("Stock contains:")
    print(f"  {stock['nickels']} nickels")
    print(f"  {stock['dimes']} dimes")
    print(f"  {stock['quarters']} quarters")
    print(f"  {stock['ones']} ones")
    print(f"  {stock['fives']} fives")


total_cents = (stock['nickels'] * 5) + (stock['dimes'] * 10) + (stock['quarters'] * 25) + (stock['ones'] * 100) + (stock['fives'] * 500)
total_dollars = total_cents // 100
total_cents_remaining = total_cents % 100
print(f"\nTotal: {total_dollars} dollars and {total_cents_remaining} cents")
