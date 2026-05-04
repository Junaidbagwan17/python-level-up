import json
from re import search
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

# ------------------------ Find Password ----------------------------------
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            searched_website = website_entry.get()
            show_details = data[searched_website]["password"]
            messagebox.showinfo(title=" Saved Password", message= f"Here is your saved password details:"
                                                                  f"\n Website: {searched_website} "
                                                                  f"\n Password: {show_details}")
    except KeyError:
        messagebox.askokcancel(title="No website found", message="Please enter valid website name that you used before!")

# ------------------ Random Password Generator ---------------------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 8))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+ password_symbols + password_numbers
    shuffle(password_list)

    new_password = "".join(password_list)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ------------------------- Save Password ---- ----------------------
def save():

    website = website_entry.get()
    email= email_entry.get()
    password =  password_entry.get()
    new_data =  {
        website: {"email": email,
                  "password":password}
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file: # to read use read for json also to dump use mode w
                # json.dump(new_data, data_file, indent=4) #WRITE
                data = json.load(data_file) # ---------------- READ
                # print(data) #dict read from saved file
                data.update(new_data) #--------------------- UPDATE old data with new data
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
                # json.dump(data, data_file, indent=4) # --------SAVING updated data
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# --------------------------- UI SETUP --------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady=50)

canvas = Canvas(width= 200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label
website = Label(text="Website:")
website.grid(column=0 , row=1,sticky="w")
email =  Label(text="Email/Username:")
email.grid(column=0, row=2, sticky="w")
password = Label(text = "Password:")
password.grid(column=0, row=3, sticky="w")

# Entry
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1,  sticky="ew",pady=5, padx=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", pady=5, padx=2)
email_entry.insert(0, 'junaid@gmail.com')
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky="ew",pady=5, padx=3)

#Buttons
generate_password_buttons = Button(text="Generate Password", borderwidth=5, command=generate_password)
generate_password_buttons.grid(column=2, row=3,padx=3, pady=5)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=5, columnspan=2, sticky="ew")
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column = 2, row=1)


window.mainloop()