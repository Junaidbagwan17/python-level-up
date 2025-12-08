student_scores = {
  "Data Visualization": 81,
  "Retail Marketing": 79,
  "Research Methodloy": 78,
  "Machine Learning": 99, 
  "Essential Tec": 74,
  "Statistics": 88,
}

# print(student_scores)

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: add the grades to student_grades.
for score in student_scores:
    if student_scores[score] > 90:
        student_grades[score] = "Oustanding"           #student_grades[score] is key   and    # outstanding is value
    elif student_scores[score] > 80:
        student_grades[score] = "exceeds expectations"
    elif student_scores[score] > 70:  
        student_grades[score] = "Accseptable"
    elif student_scores[score]<= 70:
        student_grades[score] = "Fail"

print(student_grades)

# -------------------------------

#for student in student_scores:
    # print(student) # only keys
    # print(student_scores[student]) # only Values 
    # score = student_scores[student] this can be done 
    # then check score > 90 ....