
from turtle import Turtle
import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# pull state CSV data
state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()


def write_state_name_to_map(state_name_input):
    # write state name at state xy coord
    state_map_name = Turtle()
    state_map_name.color("black")
    state_map_name.penup()
    state_map_name.hideturtle()
    state_map_name.goto((state_x_coord, state_y_coord))
    state_map_name.write(state_name_input)


def you_win():
    win_text = Turtle()
    win_text.color("red")
    win_text.penup()
    win_text.hideturtle()
    win_text.write("You got them all!", font=("Courier", 18, "normal"))


states_correct = 0
selected_states = []

while states_correct < 50:
    # dialog input for states
    answer_state = screen.textinput(title=f"{states_correct}/50 States Correct", prompt="What's another state's name?").title()
    # stop if Cancel
    if answer_state == "Cancel":
        missing_states = []
        for state in state_list:
            if state not in selected_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states to learn.csv")
        print(missing_states)
        break

    # if answer_state in state_data["state"].values:
    if answer_state in state_list and answer_state not in selected_states:
        input_state = state_data[state_data.state == answer_state]
        # Index of selected state from list, then get state name from list
        state_list_index = state_list.index(answer_state)
        state_name = state_list[state_list_index]
        # coords of state
        state_x_coord = int(input_state["x"])
        state_y_coord = int(input_state["y"])
        # write state name to state coord
        write_state_name_to_map(state_name)
        # add to score
        states_correct += 1
        # add to selected states list
        selected_states.append(answer_state)
if states_correct == 50:
    you_win()

