from turtle import Turtle, Screen
import pandas as pd
from StateNameRecord import StateNameRecord
from Scoreboard import Scoreboard

turtle = Turtle()
screen = Screen()
img_path = "./blank_states_img.gif"
screen.title("U.S. States Game")
screen.addshape(img_path) #shape can be any image file
turtle.shape(img_path)
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name? ").strip()

states_data = pd.read_csv("./50_states.csv") #pd DataFrame
states_series = states_data.state
state_name_record = StateNameRecord()
score_board = Scoreboard()
game_on = True

while game_on:
    if answer_state.lower() == "exit": #if user typed secret word 'exit'
        break

    for state in states_series:
        if (state.lower() == answer_state.lower()) and (not state in state_name_record.guessed_states):
            state_row = states_data[states_series == state]
            x = int(state_row.x) #second column
            y = int(state_row.y) #last column
            state_name_record.addState(state, x, y)
            score_board.increment_score()
    
    if score_board.score == 50:
        screen.title("Congrats! You got all 50 states correct!")
        game_on = False
        screen.exitonclick() #terminates program
    
    answer_state = screen.textinput(title=f"{score_board.score}/50 States Correct", prompt="What's another state's name? ").strip()

#states_to_learn.csv
states_to_learn = []
for state in states_series:
    if not state in state_name_record.guessed_states:
        states_to_learn.append(state)
states_to_learn = pd.DataFrame(states_to_learn)
states_to_learn.to_csv("./states_to_learn.csv")

screen.mainloop()