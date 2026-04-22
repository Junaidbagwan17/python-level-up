# TODO: create a letter using starting_letter.txt
# for each name in invited_names.txt
# replace the placeholder [name] with actual name
# save the letters into Output - Ready to send folder:
PLACEHOLDER = "[name]"

# used absolute file path below
with open("E:/Python_Github/day24/Mail-merge/Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_contents = letter_file.read()#docx

with open("E:/Python_Github/day24/Mail-merge/Input/Names/invited_names.txt" , "r") as names_file:
    names = names_file.readlines()
    # print(names)

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) # we used relative file path below
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:#docx
        completed_letter.write(new_letter)
