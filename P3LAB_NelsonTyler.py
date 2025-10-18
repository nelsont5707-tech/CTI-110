# Tyler Nelson
# 10/17/2025
# P3LAB1
# This program helps you figure out the quickest and most efficient way to break down an amount of money into dollars, quarters, dimes, nickels, and pennies.

def calculate_change(amount):
    amount_in_cents = round(amount * 100)
    
    dollars = amount_in_cents // 100
    amount_in_cents %= 100

    quarters = amount_in_cents // 25
    amount_in_cents %= 25

    dimes = amount_in_cents // 10
    amount_in_cents %= 10

    nickels = amount_in_cents // 5
    amount_in_cents %= 5

    pennies = amount_in_cents
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
    if amount_in_cents == 0:
        print("No change")

if __name__ == "__main__":

    try:
        amount = float(input("Enter float money value: $"))
        
        if amount == 0:
            print("No change")
        else:

            calculate_change(amount)
    except ValueError:
        print("Invalid input. Please enter a valid float money value.")