import random

test_seed = int(input("careate a seed"))
random.seed(test_seed)

toss = random.randint(1,2)
if toss == 1:
    print("Head")
else:
    print("Tails")