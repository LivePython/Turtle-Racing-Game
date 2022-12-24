from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
user_bet = screen.textinput('Make your bet', 'Which turtle will win the race. Pick a color').lower()

screen.setup(width=600, height=400)
color = ['red', 'blue', 'green', 'purple', 'brown', 'yellow']
location = [75, 45, 15, -15,-45, -75]
distance = [1,2,3,4,5]

turtle_list = []
for index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(color[index])
    tim.goto(x=-290, y=location[index])
    turtle_list.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 280:
            winning_color = turtle.pencolor()
            is_race_on = False
            if user_bet == winning_color:
                print(f"You won. The {winning_color} turtle won the turtle race")
            else:
                print(f"You lose. The {winning_color} turtle won the turtle race")



