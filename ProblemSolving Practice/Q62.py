# todo: Create a program that finds the common elements between two lists and stores them in a new list

list1 = [2, 13,2, 5, 6 ,8, 10]
list2 = [4, 15,2, 2, 6, 3]

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)
print(common)


