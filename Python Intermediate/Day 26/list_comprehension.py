numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers] # or directly print([....])
print(new_numbers)
#--------------------------------------------------
# todo predict the output of given code
name = "JUNAID"
new = [letter for letter in name]
print(new)
#--------------------------------------------------
# TODO:  create a new list from a range, where the list items are double values of the range
# eg. double of 2 is 4
numbers = [n for n in range(1,5)]
print("number before double:",numbers)
numbers = [n+n for n in range(1,5)]
print("number after double:", numbers)
#--------------------------------------------------
# todo:  create a list which of names which contains more than 5 char and print them uppercase
names = ["Alex", "Beth", "Jordan", "Richard", "Washington", "Sam"]
# long_names = [new_item for item in list if test]
print("Long names in CAPTIAL:")
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
#todo: create a list which contains less than 5 char
print('short names:')
short_names= [name for name in names if len(name) < 5]
print(short_names)
