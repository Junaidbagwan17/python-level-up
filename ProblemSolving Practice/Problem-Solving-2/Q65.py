# TODO: Given a list of names, remove all duplicate names and print the unique names

names = ["Alice","Bob","John","Bob"]

unique_names = []
for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)