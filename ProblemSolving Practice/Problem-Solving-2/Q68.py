 #TODO: Implement a function that takes two lists and returns their union (all unique elements from both lists)4

def union_lists(list1, list2):
    return list(set(list1 + list2))

print(union_lists([1, 2, 3], [3, 4, 5]))