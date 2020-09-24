#2.1 A “draw.py” file draws the following picture – a similar shapeshould be fine, you should use “red” and “blue” color.
import turtle
heading=180
distance=60
pen = turtle.Pen()
pen.color('red')
pen.width(5)
heading-=45
pen.setheading(heading)
pen.forward(distance)
heading-=90
pen.setheading(heading)
pen.forward(distance*3)
heading-=90
pen.setheading(heading)
pen.forward(distance)
pen.color('blue')
heading+=90
pen.setheading(heading)
pen.forward(distance)
heading-=90
pen.setheading(heading)
pen.forward(distance*3)
heading-=90
pen.setheading(heading)
pen.forward(distance)
turtle.done()