# Given a list of names, concatenate them into a single string separated by spaces

names = ["Junaid", "Bagwan", "MscDataScience"]

# 1. Using loop
single = ""
for name in names:
    single += name
print(single)

# 2 using functions
print("".join(names))