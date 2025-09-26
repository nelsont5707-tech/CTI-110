# Tyler Nelson
# 09/26/2025
# P1HW2
# This program asks for your budget, destination, and expenses to help you better financially prepare for your trip.

# Ask you how much money they have for their budget.
# Ask where you are traveling.
# Ask how much you think you'll spend on gas.
# Ask how much you'll spend on accommodation or hotel.
# Ask how much you'll spend on food.
# Add up all of the expenses.
# Subtracts the expenses from the budget to find the remaining balance.
# Show the travel destination, the starting budget, total expenses, and the remaining balance.

print("This program calculates and displays travel expenses\n")

budget = float(input("Enter Budget: "))

destination = input("\nEnter your travel destination: ")

gas = float(input("\nHow much do you think you will spend on gas? "))

accommodation = float(input("\nApproximately, how much will you need for accomodation/hotel? "))

food = float(input("\nLast, how much do you need for food? "))

total_expenses = gas + accommodation + food

balance = budget - total_expenses

print("\n------------Travel Expenses------------")

print("Location:", destination)

print("Initial Budget:", int(budget))

print()

print("Fuel:", int(gas))

print("Accomodation:", int(accommodation))

print("Food:", int(food))

print()

print("Remaining Balance:", int(balance))