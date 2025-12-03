import random

test_seed = int(input("enter seed: "))
random.seed(test_seed)

names_as_csv =  input("Names as CSV: ")
names = names_as_csv.split(",")


a = (random.randint(0, len(names)-1))
k = names[a]
print(f"{k} is going to pay the bill") 
