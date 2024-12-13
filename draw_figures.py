import turtle     #impo bibliot turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightpink")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)


side_length = 60


for i in range(4):
    pen.forward(side_length)
    pen.right(90)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()