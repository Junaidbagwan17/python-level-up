from tkinter import  *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Km")
window.config(padx=25 , pady=25)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text = "Miles")
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="Is equal to:")
equal_to_label.grid(column= 0, row=1)

km_result_label = Label(text=0, font=("Times New Romen", 9, "italic" ))
km_result_label.grid(column=1,row=1)

km_label = Label(text = "Km")
km_label.grid(column=2 , row= 1)

calculate_button = Button(text="Calculate" , font=("Times New Romen", 10, "bold" ), command=miles_to_km)
calculate_button.grid(column=1,row=2)


window.mainloop()