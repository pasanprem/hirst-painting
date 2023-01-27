# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# print(type(colors))
#
# i = 0
# color_list = []
# for i in colors:
#     rgb = i.rgb
#     color_tup = (rgb.r, rgb.g, rgb.b)
#     color_list.append(color_tup)
#
# print(color_list)

from turtle import Turtle, Screen
import random

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t = Turtle()
screen = Screen()
screen.colormode(255)
print(t.pos())
t.speed(0)
x = 0.0
y = 0.0

def fill_circle():
    t.color(random.choice(color_list))
    t.pendown()
    t.begin_fill()
    t.circle((5))
    t.end_fill()
    t.penup()

for row in range(0, 10):
    t.setposition(x, y + (row * 25))
    for _ in range(10):
        fill_circle()
        t.forward(25)


screen.exitonclick()



