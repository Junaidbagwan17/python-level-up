#TODO: Write a function to remove all duplicate characters from a given string


def remove_duplicates(text):
    result = ""
    for i in text:
        if i not in result:
            result += i
    return result
print(remove_duplicates("programming"))

# This code works, but:
# loop O(n) time and Loop runs n times so Total complexity = O(n**2)  and it is slow for large strings
# Why set is better: Lookup is O(1), Total becomes O(n)

def remove_duplicated(text):
    seen = set()
    result = []

    for i in text:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return "".join(result)
print(remove_duplicated("programming"))

