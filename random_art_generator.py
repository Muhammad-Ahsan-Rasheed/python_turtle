import turtle 
from random import randint

def input_angle(): 
    num = randint(100, 170)
    return num

def generate_random_colour(): 
    """Generates an R,G,B values randomly in range 0 to 255 """ 
    r = randint(0, 255) 
    g = randint(0, 255) 
    b = randint(0, 255) 
    return r, g, b

print('Set up Screen') 
turtle.title('Colorful pattern')
turtle.setup(1200, 800) 
turtle.hideturtle()
turtle.bgcolor('black')
turtle.tracer(4, 10)
turtle.speed(1)
turtle.pensize(5)



# Set the background colour of the screen 
turtle.colormode(255)
# Indicates RGB numbers will be in the range 0 to 255 
angle = input_angle()
print(f'Angle is {angle}')
print('Start the drawing') 
for i in range(5, 800):
    turtle.pencolor(generate_random_colour()) 
    turtle.forward(i)
    turtle.right(angle)

# turtle.pencolor('white')
# turtle.write("Zakariyan Coding Society",True, font=("Verdana", 35, "normal"))
print('Done')
turtle.done()
# [103, 154, 108, 121, 135, 160, 177, 140, 120, 144, 100, 108]