#TODO: Write a function that takes two lists and returns their intersection (common elements)

li1= [2, 3, 4, 5, 6, 7]
li2 = [2, 4, 6, 8, 10]

def find_common(list1, list2):
    result = []
    for i in list1:
        if i in list2:
            result.append(i)
    return result
print(find_common(li1,li2))


# method 2: prefer this bcz what if list has duplicates?
def find_common(list1, list2):
    return list(set(list1) & set(list2))
print(find_common(li1, li2))


