# Tyler Nelson
# 11/15/2025
# P5LAB1
# This program helps you simulate your own self checkout by generating a random amount and using how much cash you'll spend to help you get the total amount in cash change.

import random

def disperse_change(change):
    cents = round(change * 100)

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print(f"\n{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")


def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")

    cash = float(input("How much cash will you put in? "))

    change = round(cash - amount_owed, 2)
    print(f"Change is: ${change}")

    disperse_change(change)

main()
