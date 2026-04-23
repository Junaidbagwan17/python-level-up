#TODO: Create a function to find the square of each element in a given list

#method to just solve
numbers = [2 , 4, 6, 8]
squares_list = []

def square():
    for n in numbers:
        squares_list.append(n ** 2)
    print(squares_list)
square()

# method1: below should be preferred
def square(numbers):
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result

numbers = [2, 4, 6, 8]
print(square(numbers))


# method 2 also preferd
def square_list(numbers):
    result = []
    for n in numbers:
        result.append(n * n)
    return result
print(square_list([2, 4, 6, 8]))