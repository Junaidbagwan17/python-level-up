# method 1 - making ranges change by 2 
total = 0
for number in range(2, 101, 2):
    total += number
print(total) #INDENTATION MATTERS HERE!

# method 2 - using % and if condition
total2 =0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)