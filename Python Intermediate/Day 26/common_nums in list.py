# find common elements in two lists

#this method is preferred
with open("file1.txt") as file1:
    list1 = file1.readlines()

with open('file2.txt') as file2:
    list2 = file2.readlines()

result =  [int(n) for n in list1 if n in list2]
print(result)


#-----------------------------------------------------
# method 2
with open("file1.txt") as file1:
    list1 = [int(line.strip()) for line in file1 ]
# print(list1)
with open('file2.txt') as file2:
    list2 = [int(line.strip()) for line in file2 ]

print("List 1:",list1)
print("List 2:",list2)

result = [n for n in list1 if n in list2 ]
print("the common elements from two lists are:\n", result)
#----------------------------------------------------------

