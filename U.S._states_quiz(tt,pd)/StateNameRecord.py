from turtle import Turtle

class StateNameRecord(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.guessed_states = []

    def addState(self, state_name_par, x_par, y_par):
        self.goto(x_par, y_par)
        self.write(state_name_par)
        self.guessed_states.append(state_name_par)