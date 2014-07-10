import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.circle(40, steps = 3)

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps = 4)

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps = 4)

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps = 5)

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps = 5)

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps = 6)

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40)

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("green")
turtle.circle(40, steps = 5) # Draw a pentagon
turtle.end_fill() # Fill the shape


turtle.done()
