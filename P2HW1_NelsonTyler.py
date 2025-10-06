# Tyler Nelson
# 10/05/2025
# P2HW1
# This program helps you calculate your travel expenses.adaswd121211

initial_budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
fuel_cost = float(input("How much do you think you will spend on gas: "))
accommodation_cost = float(input("Approximately, how much will you need for accommodation/hotel: "))
food_cost = float(input("Last, how much do you need for food: "))
remaining_balance = initial_budget - (fuel_cost + accommodation_cost + food_cost)

print("\n-----------Travel Expenses-----------")
print(f"Location:          {destination}")
print(f"Initial Budget:    ${initial_budget:,.2f}")
print(f"Fuel:              ${fuel_cost:,.2f}")
print(f"Accommodation:     ${accommodation_cost:,.2f}")
print(f"Food:              ${food_cost:,.2f}")
print("------------------------------------")
print(f"Remaining Balance: ${remaining_balance:,.2f}")