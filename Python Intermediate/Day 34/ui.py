from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#004080"

# 1.  Create User Interface as class and create a UI SETUP

class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text = "Score:0", fg="white", bg=THEME_COLOR, font=("Ariel",12, "normal"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=290,
                                                     text="Some q text ",
                                                     font=("Ariel", 14, "italic"),
                                                     fill = THEME_COLOR
                                                     )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = PhotoImage(file="true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.right_pressed)
        self.right_button.grid(row=2, column=1)

        wrong_img = PhotoImage(file="false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.wrong_pressed)
        self.wrong_button.grid(row=2, column =0)

        self.get_next_quetion()

        self.window.mainloop()

    def get_next_quetion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_have_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached end of the quiz")
            self.right_button.config(state="disabled")

    def right_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_quetion)
