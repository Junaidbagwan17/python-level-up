# TODO: Write a Python program to count the occurrences of each element in a given list

list1 = ["A", "A", "B", "C", "A"]
list2 = [1, 1, 2, 3, 3, 4, 4, 1, 5]
count_dict = {}
for item in list1:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict)


# OR Just ---------------
from collections import Counter
count =Counter(list1)
print(count)

# --------------
print("the follwoing thing appeard most in the dict:")
print(max(count_dict, key=count_dict.get))


