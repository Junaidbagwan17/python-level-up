from tkinter import *
import pandas
import random

# ---------------------------- PICK A RANDOM WORD and Update --------------------------------------------
BACKGROUND_COLOR = "#B1DDC8"
current_card = {}
data_dict = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    orignal_data = pandas.read_csv("eng-hindi.csv")
    data_dict = orignal_data.to_dict(orient="records") # to learn
else:
    data_dict  = data.to_dict(orient="records")

def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text = "Hindi", fill ="black")
    canvas.itemconfig(card_word, text = (current_card["hindi"]), fill = "black")
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer= window.after(3000, func=flip_card)

# ---------------------- Flip the card -----------------------------------
def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = (current_card["english"]), fill = "white")
    canvas.itemconfig(card_background, image =  card_back_img)

# ------------------------------  Remove card if Known --------------------------------------------
def is_known():
    data_dict.remove(current_card)
    generate_word()
    df = pandas.DataFrame(data_dict)
    df.to_csv("words_to_learn.csv", index=False) #false becz not want index to be added

# ------------------------------  UI SETUP --------------------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50 , pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263,image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Poppins",40,"italic"))
card_word = canvas.create_text(400, 263, text= "word", font=("Times New Romen",40,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img =PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_img, command=generate_word)
unknown_button.grid(row=1, column=0)

tick_img = PhotoImage(file="right.png")
known_button= Button(image=tick_img, command=is_known)
known_button.grid(row=1, column=1)

generate_word()


window.mainloop()