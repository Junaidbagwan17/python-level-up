def format_name(f_name, l_name):# parametesr : f_name and l_name
    # conv parameters into title case
    if f_name == "" and l_name == "":
        return  "input not recived"
    formated_fname = f_name.title()
    formated_lname= l_name.title()
    return (f"{formated_fname} {formated_lname}")

# print(format_name("vIRat", "kOhLi"))
# lets take an input for name
print(format_name(input("what is first name:"), input("what is your last name: ")))
# go and edit function if user only space " "
