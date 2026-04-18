#TODO: Given a list of words, count the number of words with more than five characters

words = ["Maharashtra", "Goa", "Delhi", "Up", "Bengaluru", "Bihar"]
count = 0

for word in words:
    if len(word) > 5:
        count += 1
print(f"Number of words with more than five characters: {count}")