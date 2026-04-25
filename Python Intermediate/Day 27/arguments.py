# modify the add function to take an unlimted number of arguments.
# use a loop to sum all the argguments inside the function.
# test it out by calling add() to calculate sum of some arguments


def add(*args):
    result = 0
    for n in args:
        result += n
    return (result)

print(add(5, 5, 2,8))
