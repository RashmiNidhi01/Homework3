#2.1 A “draw.py” file draws the following picture – a similar shapeshould be fine, you should use “red” and “blue” color.
import turtle#turtle package imported
heading=180
T=turtle.Pen()
T.color('red')
T.width(5)
heading-=45
T.setheading(heading)
T.forward(60)
heading-=90
T.setheading(heading)
T.forward(180)
heading-=90
T.setheading(heading)
T.forward(60)
T.color('blue')
heading+=90
T.setheading(heading)
T.forward(60)
heading-=90
T.setheading(heading)
T.forward(180)
heading-=90
T.setheading(heading)
T.forward(60)
turtle.done()