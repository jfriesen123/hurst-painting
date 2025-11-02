import colorgram
# colour_palette = colorgram.extract('image.jpg', 50)
#
# colour_list = []
#
# for colour in colour_palette:
#     red = colour.rgb.r
#     green = colour.rgb.g
#     blue = colour.rgb.b
#     new_colour = (red, green, blue)
#     colour_list.append(new_colour)
#
# print(colour_list)

from turtle import Turtle, colormode, Screen
import random


t = Turtle()
colormode(255)


colour_list = [(192, 171, 125), (156, 177, 193), (193, 162, 176), (215, 203, 127), (154, 185, 174), (165, 207, 187),
               (208, 180, 194), (179, 189, 209), (193, 158, 50), (161, 204, 214), (109, 119, 174), (209, 182, 181), (201, 208, 37), (102, 110, 146)]

# Paint 10 x 10 picture -> dot size = 20, spaced by 50.
t.pensize(20)
steps = 50
t.speed("fastest")
t.hideturtle()

# Start (5 - 50x)(5 - 50y) from center.
t.penup()
x_axis = -225
y_axis = -225
t.sety(y_axis)
t.setx(x_axis)

# Change colour each time, Pen up and down to create dots rather than continuous line. Reset back to y-axis for each row.
for row in range(10):
    y_step = steps * (row + 1)
    for step in range(10):
        t.color(random.choice(colour_list))
        t.pendown()
        t.fd(1)
        t.penup()
        t.forward(steps)

    t.setx(x_axis)
    t.sety(y_axis + y_step)


my_screen = Screen()
my_screen.exitonclick()