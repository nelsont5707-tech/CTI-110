# Tyler Nelson
# 10/05/2025
# P2HW1
# This program asks you to enter grades for six modules, calculates and displays the lowest grade, highest grade, sum of grades, and the average grade.

# The program asks the user to enter a grade for each of the six modules.
# Calculates the lowest grade from the information given.
# Calculate the highest grade from the information given.
# Calculate the sum of all grades from the information given.
# Calculate the average by dividing the sum by the information given.
# Finally, it shows the user the results in a straightforward manner.

grades = []

grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))

grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print("-----------Results-----------")
print(f"Lowest Grade: {lowest_grade:.1f}")
print(f"Highest Grade: {highest_grade:.1f}")
print(f"Sum of Grades: {sum_of_grades:.1f}")
print(f"Average: {average_grade:.2f}")
print("----------------------------")