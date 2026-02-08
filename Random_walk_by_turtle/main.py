import turtle as t
from random import choice ,randint
# tim - is the turtle object
tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.pensize(15)
t.colormode(255)
screen = t.Screen()
screen.title("Random Walk")
screen.bgcolor("black")

def random_colour():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r,g,b)
    return color

directions = [0,90,180,270]
for _ in range(300):
    steps = randint(10,30)
    tim.color(random_colour())
    tim.setheading(choice(directions))
    tim.forward(steps)

screen.exitonclick()

