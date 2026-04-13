# TODO Q9 Given a list of integers, find the sum of all positive numbers

scores = [70, 80, 76, 21, 20, 86, 43, 49, 41]

#1.  using sum function
total = sum(scores)
print(f"the sum of all positive integers is {total}")

#2.  using loop
total2 = 0
for i in scores:
    total2 += i
print(f"the sum of all positive integers is {total2}")

#3. using function
def add(li):
    total3 = 0
    for i in li:
        total3 += i
    return (f"the sum of all positive integers is {total3}")
result = add([70, 80, 76, 21, 20, 86, 43, 49, 41])
print(result)
