student_scores = input("enter scores: ").split()

for n in range(0 , len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_Score = 0
for score in student_scores:
    if score > highest_Score:
        highest_Score = score
        
print(f"The score in the class is {highest_Score}.")

