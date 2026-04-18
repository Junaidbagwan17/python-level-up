# todo: Create a loop that prints all prime numbers between 1 and 50

for num in range(1,51):

    if num > 1:
        for i in range(2, num):
            if num %  i == 0:
                break
        else:
            print(num)