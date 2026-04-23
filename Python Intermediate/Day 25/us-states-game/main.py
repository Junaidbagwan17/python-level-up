import  turtle
import pandas

sc = turtle.Screen()
sc.title("U.S. States Game")
image = "blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)

gussed_states = []
data = pandas.read_csv("./50_states.csv")
states_list = data.state.to_list()


while len(gussed_states) < 50:
    answer_states = sc.textinput(title=f"{len(gussed_states)}/50 the States.",
                                 prompt="Whats the another states's name?")
    guess = answer_states.title()

    if guess == "Exit":
        missing_states = []
        for state in states_list:
            if state not in gussed_states:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("missing_states.csv")
        break

    if guess in states_list:
        gussed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(guess)

# sc.exitonclick()
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
