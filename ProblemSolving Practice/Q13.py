# TODO : Given a list of numbers, find the sum and average

numbers = [80 , 85, 90 , 78 , 90, 89]

# find sum
total = 0
for i in numbers:
    total += i
print("sum of the list:",total)

# find len
total_count = 0
for n in numbers:
    total_count += 1
print("total length of numbers:",total_count)

# find avg
average = round(total / total_count)
print(f"The average numbers in list is {average}")
