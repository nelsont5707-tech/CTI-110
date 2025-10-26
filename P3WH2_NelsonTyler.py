# Tyler Nelson
# 10/26/2025
# P3WH2
# This program calculates your employee's regular pay and gross pay if they worked overtime.

# Asks you to enter the employee's name
# Ask you to enter number of hours they worked
# Ask you to enter pay rate and if there was any overtime hours worked
# Calculate regular pay or gross pay if there was overtime

employee_name = input("Enter employee's name: ")

hours_worked = float(input("Enter the number of hours worked: "))

pay_rate = float(input("Enter the employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

else:
    overtime_hours = 0
    regular_hours = hours_worked
    overtime_pay = 0

regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

print("---------------------------------------------")
print(f"Employee name:  {employee_name}")
print()
print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("-------------------------------------------------------------------------------")
print(f"{hours_worked:<14.1f}{pay_rate:<11.2f}{overtime_hours:<11.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:.2f}")
