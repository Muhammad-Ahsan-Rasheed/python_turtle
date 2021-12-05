import turtle 
from random import randint
import random

turtle.title('Colorful pattern')
turtle.setup(1270, 950, 0, 0)
turtle.hideturtle()
turtle.bgcolor('black')
turtle.tracer(4, 10)
turtle.speed(15)
turtle.pensize(10)

turtle.colormode(255)
angle = [103, 154, 108, 121, 135, 160, 177, 140, 120, 144, 100, 108, 276, 90, 289]
s_angle = random.choice(angle)
color = ['indigo', 'blue', 'green', 'yellow', 'orange', 'red']
for i in range(5, 800):
    turtle.pencolor(color[i % len(color)]) 
    turtle.forward(i)
    turtle.right(s_angle)

turtle.done()
