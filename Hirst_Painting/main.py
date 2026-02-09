# import colorgram
# colors = colorgram.extract('practice.jpg',30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as t_module
import random
tim = t_module.Turtle() # tim is the object.
t_module.colormode(255)
tim.speed("fastest")
tim.up()
tim.hideturtle()
color_extracted = [(185, 162, 132), (129, 92, 70), (79, 93, 118), (147, 161, 180), (179, 152, 162), (210, 207, 135), (28, 35, 49), (119, 79, 92), (54, 24, 33), (46, 25, 19), (147, 170, 154), (86, 107, 91), (161, 156, 60), (113, 31, 43), (168, 107, 98), (27, 37, 33), (51, 58, 92), (212, 179, 189), (110, 123, 155), (117, 37, 27), (161, 107, 118), (219, 178, 170), (177, 202, 186), (180, 187, 209), (106, 144, 116), (67, 75, 35)]

tim.setheading(225)
tim.forward(400)
tim.setheading(0)
number_of_dots = 100

for dot_counts in range(1,number_of_dots+1):
    tim.dot(15,random.choice(color_extracted))
    tim.forward(50)

    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t_module.Screen()
screen.exitonclick()
