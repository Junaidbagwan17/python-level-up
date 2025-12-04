students_heights = input("enter the heights of the students : ").split()

# converting list into Integer
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])  
print(students_heights) 

# create a null variable and add heights
total = 0
for height in students_heights:
    total += height
print(total) 

# create a null variable and add by one only to get counts
n = 0
for student in students_heights:
    n += 1
print(n)

# Average / Mean 
avg_heights = round((total / n), 2)

# print(round(avg_heights ,2))
print(f"Average Height of the student is {avg_heights}")