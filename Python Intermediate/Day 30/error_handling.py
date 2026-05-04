# # we sometimes have errors like KeyError TypeError and all
#
# # FileNotFoundError -- > we had this a while ago many times
# with open("a_file.txt") as file:  # this file dosent exist in directory so it will cause an error
#     file.read()
#
# # KeyError -- > when there is no such key in dict
# a_dict = {"India":"Delhi"}
# print(a_dict["Russia"])   # no russia key exists in dict so key error
#
# # IndexError  -- > when you try to get index which dose not exaist
# fruits = ["apple", "cherry", "mango"]
# print(fruits[3]) # no third index exist bcz we start from 0 in python
#
# # TypeError  -- > happens when you try to deal with int and str once
# text = "abcd"
# nums = 1234
# print(text+nums)

# ---------------- How to deal with these errors ----------------
# let suppose we have FileNotFoundError to handle it we use try and except blocks

#-------------------- Scenario 1: File Not Found Error
# try:
#     file = open("a_file.txt") # this file we assume is there in diretory but its not
# except:
#     file = open("a_file.txt", 'w') # so we will handle by creating new file in exception block.



#-------------------- Scenario 2: FileNotFoundError and Key error
# try:
#     file = open("a_file.txt")  #this file does exist bus,
#     a_dict = {"India": "Delhi"}
#     print(a_dict["sdfsdf"]) # Key error
#
# except:
#     file = open("a_file.txt", "w")
#     file.write("Hello World") # we wrote into file but what about KeyError that was totally ignored?

#------------------ Scenario 3: How to fix another Error in Try Block and Else and final block
try:
    file = open("a_file.txt")  # this file does exist bus,
    a_dict = {"India": "Delhi"}
    print(a_dict["India"])  # Key error when you use #sdsdfsdf

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Hello World")

# except KeyError:
#     print("No such Key in the Dictionary")

except KeyError as error_msg:
    print(f"key; {error_msg} not found in the dictionary!")

else: # when nothing fails do this -  it will work and print only when we specify a correct key 'India'
    content = file.read()
    print(content)

finally: # no matter what fails or not do this -- garunteed execution
    file.close()
    print("File was closed")
