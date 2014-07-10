# Prompt
x1, y1 = eval(input("Enter 1st x, y coordinates: "))
x2, y2 = eval(input("Enter 2nd x, y coordinates: "))

distance = round(((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5, 2)

print("Distance between, ", x1, y1, "and ", x2, y2, "is: ", distance)

import turtle
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2, y2)
turtle.write("Point 2")
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)

turtle.done()
             
