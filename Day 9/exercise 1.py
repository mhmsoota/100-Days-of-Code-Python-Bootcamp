student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

from math import ceil

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  if ceil(student_scores[key]) in range(91,101):
    student_grades[key] = "Outstanding"
  elif ceil(student_scores[key]) in range (81,91):
    student_grades[key] = "Exceeds Expectations"
  elif ceil(student_scores[key]) in range(71,81):
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"    

# 🚨 Don't change the code below 👇
print(student_grades)
