from collections.abc import tuple_iterator
from tkinter import *

# create a new window and confitg
window = Tk()
window.title("Widget Demo")
window.minsize(height=300, width=500)

# Labels
label = Label(text="this is old text")
label.config(text="this is new text")
label.pack()

# Buttons
def action():
    print("do something")

# calls action() when pressed
buttons = Button(text = "click me", command = action)
buttons.pack()

# entries
entry = Entry(width=30)
# add some text to begin
entry.insert(END, string="Some text to begin")
# get text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# puts cursser in text box
text.focus()

# add some text to begin with
text.insert(END, "Example multiline text entrey.")

# gets curent value in textbox at line 1 char0
print(text.get("1.0",END))
text.pack()


# spindbox
def spinbox_used():
    print(spinbox.get())
    # gets the current value in spinbox
spinbox = Spinbox(from_=0 , to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0 , to = 100, command=scale_used)
scale.pack()

# checkbuttons
def check_button_used():
    # prints 1 on button checked else prints 0.
    print(check_state.get())

# var to hold on to checked state 0 is off 1 is on 0 is off
check_state = IntVar()
checkbutton = Checkbutton(text= "Is on ?", variable=check_state, command=check_button_used)
checkbutton.pack()

# RadioButton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()

radiobutton1 = Radiobutton(text= 'Option1', value=1, variable=radio_state, command=radio_used())
radiobutton2 = Radiobutton(text= 'Option2', value=2, variable=radio_state, command=radio_used())
radiobutton1.pack()
radiobutton2.pack()

# list box
def list_box_used(event):
    print(listbox.get(listbox.curselection()))
    # get current selection form Listbox

listbox =  Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", list_box_used)
listbox.pack()

window.mainloop()