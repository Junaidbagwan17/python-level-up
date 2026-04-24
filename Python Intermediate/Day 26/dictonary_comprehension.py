import random
# {new_key: new_value for item in list
names = ["Alex", "Bob", "Momo", "Jack"]
student_score = {student:random.randint(1, 100) for student in names}
print(student_score)

#{ new_key:new_value for (key,value) in dictionary.items() if test }
passed_students = {student:score for (student,score) in student_score.items() if score > 60 }
print(passed_students)