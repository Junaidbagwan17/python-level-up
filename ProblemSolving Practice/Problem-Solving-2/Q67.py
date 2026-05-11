 # TODO: Write a program that checks if a given list is sorted in ascending order

def is_sorted(numbers):
    for i in range(len(numbers) -1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4]))
print(is_sorted([1, 23, 7, 83]))