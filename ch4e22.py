import turtle

x2, y2 = eval(input("Enter point: "))

distance = ((x2 - 0) ** 2 + (y2 - 0) ** 2) ** 0.5 

if distance <= 10:
    print("Point", x2, y2, "is within the circle")
else:
    print("Point", x2, y2, "is not within the circle")

turtle.goto(0, 0)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.dot(5, "red")
turtle.hideturtle()
