from tkinter import *
import requests

def get_quotes():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text= quote)

# ---------------------------- UI SETUP --------------------------------------
window =  Tk()
window.title("Kanye Says..")
window.config(pady=50, padx=50)

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="background.png")
canvas.create_image(150, 207 , image = background_image, )
quote_text = canvas.create_text(150, 207, text= "Some text to get started",  width=250, font=("Courier" ,20))
canvas.grid(row=0, column=0)
get_quotes()
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quotes)
kanye_button.grid(row=1, column=0)


window.mainloop()
