from turtle import Turtle
from random import choice

tim = Turtle()
tim.shape("turtle")

def n_sides(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
colours = ["red", "green" ,"blue", "yellow", "skyblue","green"]
for i in range(3,11):
    tim.color(choice(colours))
    n_sides(i)