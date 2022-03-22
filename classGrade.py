"""LAMENS
start
create a last to store 5 numbers (float)
capture user's input times for their grades
each time we capture the user's input, we append the number to the list
sort the list ascending, then splice the items starting at index 2
once we have the three highest numbers in the list, sum them, then divide by the remainder
output a message to the user
end
"""
"""PSUDOCODE
create a list
(capture input
append number to list) five times

"""

grades = []

grade = input("enter the 1st grade")
grades.append(float(grade))
grade = input("enter the 2nd grade")
grades.append(float(grade))
grade = input("enter the 3th grade")
grades.append(float(grade))
grade = input("enter the 4th grade")
grades.append(float(grade))
grade = input("enter the 5th grade")
grades.append(float(grade))

grades.sort()

grades = grades[2:]
grades = sum(grades)
avgGrade = grades / 3
print("Average grade is {0:.2f}".format(avgGrade))
