# READING FILE ONLY
file = open("../my_file.txt")
contents = file.read()
print(contents)
file.close() #
#----------------------------
# using WITH and AS
with open("../my_file.txt") as file:
    contents = file.read()
    print(contents)
#----------------------------
# write the file using MODE = "w" # but all text will be deleted for this write
with open("../my_file.txt", mode="w") as file:
    file.write("Hello is written here just now using mode 'r'")
#---------------------------
# USE APPEND FOR ADDING NEW TEXT OR NEW ITEM to file use MODE = "a"
#---------------------------
# CREATE NEW FILE IN A EXSISTING FOLDER:
with open("../new_file.txt", mode="w") as newfile:
    newfile.write("CREATED NEW FILE. using mode = 'w'")

