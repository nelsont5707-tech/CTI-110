# Tyler Nelson
# 09/27/2025
# P1HW1
# This code gets a base number and an exponent then does the calculation. After that, it will then ask for three integers to do addition and subtraction.

print("-----Calculating Exponenets----")

base = int(input("Enter an integer as the base value: "))

exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print()

print(base, "raised to the power of", exponent, "is", result, "!!")

print()

print("-----Addition and Subtraction----")

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

final_result = num1 + num2 - num3

print()

print(num1, "+", num2, "-", num3, "is equal to", final_result)