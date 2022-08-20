import turtle

# Objective of this project is to use Turtle library to draw polygons 

def polygon(turt, lenght, sides):

    ''' Draws a regural polygon of n sides with x lenght and with a turtle turt'''

    for repetition in range(0, sides):
        turt.forward(lenght)
        turt.left(360 / sides)

#Alice is a turtle.

alice = turtle.Turtle()

# Calls the polygon fuction and select alice to draw

polygon(alice, 100, 10)

#Version 2.0

turtle.mainloop()
