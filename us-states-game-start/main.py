import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
a = None
correct_guesses = []
list_of_states = data.state.to_list()
while len(correct_guesses) <= 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 states", prompt="What's another state name?").title()
    if answer_state in list_of_states:
        tim = turtle.Turtle()
        tim.pu()
        tim.ht()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)
        correct_guesses.append(answer_state)
        score = len(correct_guesses)
    elif answer_state == "Exit":
        states_not_answered = [i for i in list_of_states if i not in correct_guesses]
        data3 = pd.DataFrame(list(states_not_answered))
        data3.to_csv("Missing_states.csv")
        break


screen.exitonclick()