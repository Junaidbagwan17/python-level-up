from tkinter import *
window = Tk()

window.title("My first GUI Program")
window.minsize(height=300, width=500)
# window.config(padx=100, pady=200)

# label
my_label = Label(text="I am a Label", font=("Times New Romen", 24, "bold"))
my_label["text"] = "New Label"
my_label.config(text="New Text")
my_label.grid(column = 0, row= 0)
my_label.config(padx=50, pady=50)

# Button
def clicked_button():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=clicked_button)
button.grid(column=1,row=1)
new_button = Button(text="New Button")
new_button.grid(column=2, row=1)

#Enrty
input= Entry(width=10)
input.grid(column=2, row=2)
# print(input.get())





window.mainloop()