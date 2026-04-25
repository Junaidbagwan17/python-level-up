import tkinter
window = tkinter.Tk()

window.title("My first GUI Program")
window.minsize(height=300, width=500)

my_label = tkinter.Label(text="I am a Label", font=("Times New Romen", 24, "bold"))
my_label.pack(side="left")

window.mainloop()