# Tyler Nelson
# 10/05/2025
# P2LAB2
# This program calculates gas usage based on your vehicle choice (Camaro, Prius, Model S, Silverado) and how many miles you plan to drive it.

vehicle_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = vehicle_mpg.keys()
print(keys)

vehicle = input("Enter a vehicle to see it's mpg: ")
mpg = vehicle_mpg[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.")

miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))
gallons = miles / mpg
print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
