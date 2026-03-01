import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(600,400)
polygon=turtle.Turtle()
side = 6
length = 70
angle = 360.0/side
for i in range(side):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()    