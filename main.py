import turtle as t
import random

tim = t.Turtle()
tim.shape("square")
tim.hideturtle()
tim.penup()
tim.setposition(-230.00, -200.00)
colors = ["blue", "yellow green", "beige", "maroon", "orange", "dark sea green", "crimson", "pale violet red",
          "medium violet red", "orchid", "saddle brown", "cornsilk", "salmon", "antique white", "violet",
          "dark khaki", "rosy brown", "medium aquamarine", "royal blue", "green", "powder blue", "black",
          "dim gray", "khaki", "yellow", "dark slate blue", "lavender", "linen", "chocolate", "pale green"]


def create_dots():
    for i in range(10):
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(50)
        tim.pendown()


def move_up(x):
    tim.penup()
    tim.setposition(-230.00, -200.00 + 50.00*float(x+1))
    tim.pendown()


for i in range(10):
    create_dots()
    move_up(i)

screen = t.Screen()
screen.exitonclick()
