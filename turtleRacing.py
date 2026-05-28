from turtle import Turtle, Screen
import random as rd
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make Your bet",prompt="Which color turtle do you think will win ? Enter a color :")
colors = ["red","orange","green","blue","yellow","purple"]
turtles = []

if user_bet:
    is_race_on = True


for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240,y = -100 + 40 * i)
    new_turtle.pendown()
    turtles.append(new_turtle)

while is_race_on :
    for turtle in turtles :
        if turtle.xcor() > 230 :
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You're Guess is correct !! {winner_color} Turtle Won the race ")
            else:
                print(f"You're Guess is not correct !! {winner_color} Turtle Won the race ")
        turtle.penup()
        distance = rd.randint(1,10)
        turtle.forward(distance)

screen.exitonclick()
