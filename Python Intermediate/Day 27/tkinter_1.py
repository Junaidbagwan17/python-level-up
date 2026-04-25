from tkinter import *
window = Tk()

window.title("My first GUI Program")
window.minsize(height=300, width=500)

my_label = Label(text="I am a Label", font=("Times New Romen", 24, "bold"))
my_label.pack()

my_label["text"] = "New Label"
my_label.config(text="New Text")

# Button
def clicked_button():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=clicked_button)
button.pack()

#Enrty
input= Entry(width=10)
input.pack()
# print(input.get())




window.mainloop()