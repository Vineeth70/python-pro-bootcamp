import turtle as t
import random as rd
# tim - is the turtle object
tim = t.Turtle()
tim.speed("fastest")

t.colormode(255)
screen = t.Screen()

def random_colour():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    color = (r,g,b)
    return color

def draw_spirograph (size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
screen.exitonclick()