# Tyler Nelson
# 10/26/2025
# P3WH1
# This program takes your grades from modules one through six an finds the lowest, highest, average and total an then shows you the results.

# Asks you to enter grades for modules one through six an stores grades in a list.
# Helps you calculate your lowest, highest and average grade.
# Determines your letter grade (A,B,C,D,F) and neatly displays your results back to you.

mod_1 = float(input('Enter grade for Module 1: '))

mod_2 = float(input('Enter grade for Module 2: '))

mod_3 = float(input('Enter grade for Module 3: '))

mod_4 = float(input('Enter grade for Module 4: '))

mod_5 = float(input('Enter grade for Module 5: '))

mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

print('------------Results------------')
print(f'Lowest Grade:      {low:.1f}')
print(f'Highest Grade:     {high:.1f}')
print(f'Sum of Grades:     {total:.1f}')
print(f'Average:           {avg:.2f}')
print('--------------------------------')

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')