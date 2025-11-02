# Tyler Nelson
# 11/02/2025
# P4HW1
# This program allows the user to enter multiple scores, removes the lowest score given, and then it gives them their average and letter grade.

# The program asks the user how many scores they'd like to use, and ensures they're valid.
# It then creates an empty list to store the scores by using a loop to collect them all.
# Calculates the lowest score from the information given and drops it.
# Calculate the average by dividing the sum by the information given.
# Finally, it shows the user the results in a straightforward manner with a letter grade.

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(num_scores):
    print(f"Enter score #{i + 1}: ", end="")
    score = float(input())

    while score < 0 or score > 100:
        print("INVALID score entered! Score should be between 0 and 100.")
        print(f"Enter score #{i + 1} again: ", end="")
        score = float(input())
    
    scores.append(score)

print("\n---------- Results ----------")
print(f"Lowest Score  : {min(scores)}")

scores.remove(min(scores))
print(f"Modified List : {scores}")

average = sum(scores) / len(scores)
print(f"Average Score : {average:.2f}")

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Letter Grade  : {grade}")
print("-----------------------------")