# Tyler Nelson
# 11/02/2025
# P4LAB2
# This program shows the user a multiplication table for integers using loops, but does not compute negative ones.

run_again = "yes"

while run_again.lower() == "yes":
    num = int(input("Enter an integer: "))

    if num < 0:
        print("This program does not handle negative numbers.")
    else:
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")

    print()
    run_again = input("Would you like to run the program again? ").lower()
    print()

print("Exiting program...")