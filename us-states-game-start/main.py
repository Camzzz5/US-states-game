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

while len(correct_guesses) <= 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 states", prompt="What's another state name?").title()
    for i in data.state.to_list():
        if i == answer_state:
            tim = turtle.Turtle()
            tim.pu()
            tim.ht()
            state_data = data[data.state == answer_state]
            tim.goto(int(state_data.x), int(state_data.y))
            tim.write(answer_state)
            correct_guesses.append(i)
            score = len(correct_guesses)
    print(a)
            
            







screen.exitonclick()