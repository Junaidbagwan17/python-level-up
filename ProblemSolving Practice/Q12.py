# tODO: Create variables for storing a person's name, age, and average test score
from ET.tuples import fruits

name = "Junaid Bagwan"
age = 21
test_score = 80

#Todo: Concatenate the two string and print the result

name1 = "JuNAID".title()
name2 = " BAgwaN".title()

print(name1 + name2)

# TODO: Create a list of fruits and access elements using indexing.

fruits = ["apple", "mango", "cherry", "watermelon", "banana"]
print(fruits[0]) # apple
print(fruits[-1]) # banana
print(fruits[1:4]) # magao to watermelon
print(fruits[::-1]) # reverse
print(fruits[0::2]) #step size -- ['apple', 'cherry', 'banana']
print(fruits[:-1:]) # cant print the last one item

