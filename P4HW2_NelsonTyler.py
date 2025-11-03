# Tyler Nelson
# 11/02/2025
# P4HW2
# This program calculates employees regular and overtime paychecks.

# Gives the user the total regular overtime, and gross pay for their employees
# It'll ask for the employees names, hours worked, and pay rates and overtime pay if needed
# Finally, it shows the user the total employees, regular, overtime, and ross pay

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    
    employee_name = input('Enter employees name or "Done" to terminate: ')
    
   
    if employee_name.lower() == 'done':
        break

    
    hours_worked = float(input(f'How many hours did {employee_name} work? '))
    pay_rate = float(input(f'What is {employee_name}\'s pay rate? '))


    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
    else:
        regular_hours = hours_worked
        overtime_hours = 0
    
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

    
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

    
    print(f'\nEmployee name: {employee_name}')
    print(f'Hours Worked  Pay Rate  Overtime  Overtime Pay  RegHour Pay  Gross Pay')
    print('-------------------------------------------------------------')
    print(f'{hours_worked:10.1f}  {pay_rate:9.2f}  {overtime_hours:8.1f}  {overtime_pay:12.2f}  {regular_pay:10.2f}  {gross_pay:10.2f}')
    print()


print(f'Total number of employees entered: {employee_count}')
print(f'Total amount paid for overtime: ${total_overtime_pay:.2f}')
print(f'Total amount paid for regular hours: ${total_regular_pay:.2f}')
print(f'Total amount paid in gross: ${total_gross_pay:.2f}')
