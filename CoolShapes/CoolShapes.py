import turtle
import random

def draw_polygon(turtle_1, turtle_2, sides, length):
    for i in range (sides):
            turtle_1.left(360 / sides)
            turtle_2.left(360 / sides)
            turtle_1.forward(length)
            turtle_2.forward(length)

def draw_rotational_copy(turtle_1, turtle_2):
    copies = int(input("Enter rational copies: "))
    sides = int(input("Enter sides per polygon: "))
    length = int(input("Enter edge pixel length: "))
    for i in range(copies):
        draw_polygon(turtle_1, turtle_2, sides, length)
        turtle_1.right(360 / copies)
        turtle_2.right(360 / copies)
    turtle_1.hideturtle()
    turtle_2.hideturtle()

def choose_color(wn):
    color_options = [0.00, 0.125, 0.25, 0.375, 0.5]
    c1 = random.choice(color_options)
    c2 = random.choice(color_options)
    c3 = random.choice(color_options)
    if c1 == 0 and c2 == 0 and c3 == 0:
        choose_color()
    else:
        wn.bgcolor(c1, c2, c3)
    print("Random background color is:(", c1, c2, c3, ")")

def main():
    _Screen = turtle.Screen()
    choose_color(_Screen)

    #turtle 1 
    megan = turtle.Turtle()
    megan.color("white")
    megan.pensize(3)
    megan.speed(0)

    #turtle 2
    george = turtle.Turtle()
    george.pensize(1)
    george.speed(0)

    draw_rotational_copy(megan, george)
    
    print("Click turtle screen to exit...")
    _Screen.exitonclick()

main()



